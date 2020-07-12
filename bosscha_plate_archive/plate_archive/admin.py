from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin

from .models import Plate, StarObject

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
    inlines = (StarInline,)
    list_display = (
        'no_plate',
        'cover_tag',
        'plate_tag',
        'checked',
    )
    list_editable = (
        'checked',
    )
    resource_class = PlateResource

class StarObjectAdmin(ImportExportModelAdmin):
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
        'date',
        'plate__checked'
    )
    search_fields = (
        'star_object',
        'date'
    )

    resource_class = StarObjectResource
    
admin.site.register(Plate, PlateAdmin)
admin.site.register(StarObject, StarObjectAdmin)

