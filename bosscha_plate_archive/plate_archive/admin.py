from django.contrib import admin
from django.contrib.admin.widgets import AdminTimeWidget
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin

from .models import *

class StarObjectResource(resources.ModelResource):
    class Meta:
        model = StarObject

class PlateResource(resources.ModelResource):
    class Meta:
        model = Plate

class StarInline(admin.StackedInline):
    model = StarObject
    extra = 0

class PlateAdmin(ImportExportModelAdmin):
    """Class for Plate Admin Page"""
    def is_status(self, instance):
        instance.cover_path = os.path.join(BASE_DIR, 'media', 'plate', str(instance.plate_id), str(instance.cover_pic))
        if os.path.exists(instance.cover_path):
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
    list_display = ( *list_field, )
    list_editable = (
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
        'cover_note',
        'checked',
    )
    list_filter = (
        'cover_prog',
        'meas_auth',
        'status',
        'date_modified',
        'checked',
    )
    resource_class = PlateResource

class StarObjectAdmin(ImportExportModelAdmin):
    """Class for Star Object Admin Page"""

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


admin.site.register(Plate, PlateAdmin)
admin.site.register(StarObject, StarObjectAdmin)