from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper

from .models import Plate, StarObject


class PlateUpdateForm(forms.ModelForm):
    class Meta:
        model = Plate
        fields = [
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
        ]

    def __init__(self, *args, **kwargs):
        super(PlateUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-5'


class ObjectUpdateForm(forms.ModelForm):
    class Meta:
        model = StarObject     
        fields = [
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
        ]
    
    def __init__(self, *args, **kwargs):
        super(ObjectUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-5'