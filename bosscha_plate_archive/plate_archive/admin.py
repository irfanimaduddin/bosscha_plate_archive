from django.contrib import admin
from django.contrib.admin.widgets import AdminTimeWidget
from import_export import resources, fields, widgets
from import_export.admin import (
    ImportExportModelAdmin,
    ImportExportActionModelAdmin
)
from astropy.io import fits
from astropy.time import Time

from .models import *


class PlateResource(resources.ModelResource):
    class Meta:
        model = Plate

class StarObjectResource(resources.ModelResource):
    class Meta:
        model = StarObject

class StarInline(admin.StackedInline):
    model = StarObject
    extra = 0

class PlateAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Plate Admin Page"""
    def is_status(self, instance):
        instance.cover_path = os.path.join(BASE_DIR, 'media', 'plate', str(instance.plate_id), str(instance.cover_pic))
        if os.path.exists(instance.cover_path):
            if instance.checked == True:
                instance.status = 'Processed'
            else:
                instance.status = 'Available'
            instance.save()
            return instance.status
        else:
            instance.status = 'Unavailable'
            instance.save()
            return instance.status

    is_status.short_description = u"status"
    
    inlines = (
        StarInline,
    )
    
    actions = None

    list_field = (
        'plate_id',
        'cover_id',
        'cover_object',
        'cover_ra',
        'cover_dec',
        'cover_t_start',
        'cover_t_end',
        'cover_exp',
        'cover_emul',
        'cover_filter',
        'cover_grat',
        'cover_date',
        'cover_prog',
        'cover_obs',
        'meas_auth',
        'meas_date',
        'plate_qual',
        'cover_note',
        'cover_tag',
        'plate_tag',
        'preview_tag',
        'logbook_tag',
        'is_status',
        'date_modified',
        'checked',
    )
    list_display = ( 
        'is_status',
        'plate_id',
        'cover_tag',
        'plate_tag',
        'preview_tag',
        'logbook_tag',
        'date_modified',
        'checked',    
    )
    list_editable = (
        'checked',
    )
    list_filter = (
        'status',
        'date_modified',
        'checked',
    )
    
    resource_class = PlateResource

    list_per_page = 10

    inline_starobject = []

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def get_plateinfo(self, obj=None):
        # Convert queryset into a list for header input
        # List queryset:
        # 0 = plate_id
        # 1 = cover_id
        # 2 = cover_object
        # 3 = cover_ra
        # 4 = cover_dec
        # 5 = cover_t_start
        # 6 = cover_t_end
        # 7 = cover_exp
        # 8 = cover_emul
        # 9 = cover_filter
        # 10 = cover_grat
        # 11 = cover_date
        # 12 = cover_prog
        # 13 = cover_obs
        # 14 = meas_auth
        # 15 = meas_date
        # 16 = plate_qual
        # 17 = cover_note
        # 18 = cover_pic
        # 19 = plate_pic
        # 20 = preview_pic
        # 21 = logbook_pic
        # 22 = date_modified

        plate_id = obj.plate_id
        cover_id = obj.cover_id
        cover_object = obj.cover_object
        cover_ra = obj.cover_ra
        cover_dec = obj.cover_dec
        cover_t_start = obj.cover_t_start
        cover_t_end = obj.cover_t_end
        cover_exp = obj.cover_exp
        cover_emul = obj.cover_emul
        cover_filter = obj.cover_filter
        cover_grat = obj.cover_grat
        cover_date = obj.cover_date
        cover_prog = obj.cover_prog
        cover_obs = obj.cover_obs
        meas_auth = obj.meas_auth
        meas_date = obj.meas_date
        plate_qual = obj.plate_qual
        cover_note = obj.cover_note

        if obj.plate_pic is not str:
            cover_pic = str(obj.cover_pic)
            plate_pic = str(obj.plate_pic)
            preview_pic = str(obj.preview_pic)
            logbook_pic = str(obj.logbook_pic)

        if obj.date_modified is not str:
            date_modified = Time(obj.date_modified)
            date_modified = str(date_modified.fits)

        plate_info = [
            plate_id,
            cover_id,
            cover_object,
            cover_ra,
            cover_dec,
            cover_t_start,
            cover_t_end,
            cover_exp,
            cover_emul,
            cover_filter,
            cover_grat,
            cover_date,
            cover_prog,
            cover_obs,
            meas_auth,
            meas_date,
            plate_qual,
            cover_note,
            cover_pic,
            plate_pic,
            preview_pic,
            logbook_pic,
            date_modified
        ]
        return plate_info
        
    def get_starobject(self, obj=None):
        inline_starobject = StarObject.objects.filter(plate=obj.id).values()
        starobj1, starobj2 = inline_starobject

        # for inline in inline_starobject: # Ada berapa star object untuk plate tersebut
        #     for apa in inline: # Isi masing-masing star object
                # print(apa, ':', inline[apa])
        return inline_starobject

    def get_fitsfile(self, obj=None):
        plate_path = os.path.join(BASE_DIR, 'media', 'plate', str(obj.plate_id), str(obj.plate_pic))
        if os.path.exists(plate_path):
            plate_file = fits.open(plate_path)
            header = plate_file[0].header 
        else:
            header = None
        return header

    def header_plate(self):
        return None
        
    def header_starobj(self):
        return None

    def save_model(self, request, obj, form, change):
        obj.user = request.user.get_full_name() # GET user full name
        inst = Plate.objects.filter(id=obj.id)
        # inline_starobject = StarObject.objects.filter(plate=obj.id).values()
        # print(obj.user, obj.plate_id)
        plateinfo = self.get_plateinfo(obj=obj)
        starobject = self.get_starobject(obj=obj)
        for k, v in [(k, v) for x in starobject for (k, v) in x.items()]:
            print(k, v)
        # print(starobject['star_object'])
        # print(plateinfo)
        # print(self.get_fitsfile(obj=obj))
            
        # for inline in inline_starobject: # Ada berapa star object untuk plate tersebut
        #     for apa in inline: # Isi masing-masing star object
                # print(apa, ':', inline[apa])
        # obj.plate_id = obj.plate_id
        header = self.get_fitsfile(obj=obj)
        # print(starobject)
        # hdr_plate.close()
        super().save_model(request, obj, form, change)
        return




class StarObjectAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Star Object Admin Page"""
    
    actions = None
    list_field = (
        'plate',
        'star_object',
        'date',
        'ra',
        'dec',
        'dec_obs',
        'ha',
        't_start',
        't_end',
        'exposure',
        'temperature',
        'focus',
        'staand_plaat',
        'emulsion',
        'emulsion_no',
        'film',
        'plate_size',
        'camera_filter',
        'grating',
        'transparency',
        'seeing',
        'observer',
        'remarks',
    )
    list_editable = ( *list_field, )
    list_display = ('id', *list_field)
    list_filter = (
        'plate',
        'date',
        'plate__checked'
    )
    search_fields = (
        'plate',
        'star_object',
        'date'
    )

    resource_class = StarObjectResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
        
    # def save(instance, *args, **kwargs):
    #     print(instance.star_object)
    #     super().save(*args, **kwargs)


admin.site.register(Plate, PlateAdmin)
admin.site.register(StarObject, StarObjectAdmin)