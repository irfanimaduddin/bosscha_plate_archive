from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.views.generic import (
    ListView, 
    DetailView, 
    TemplateView,
    UpdateView
)

from .models import Plate, StarObject
from .form import PlateUpdateForm, ObjectUpdateForm

class HomeView(TemplateView):
    """ A class for Home View"""
    template_name="main/home.html"

class PlateListView(ListView):
    """ A class for Plate List View"""
    template_name = "main/index.html"
    queryset = Plate.objects.all()
    
    def get(self, request, *args, **kwargs):
        context={"queryset": self.queryset}
        return render(request, self.template_name, context)


class PlateObjectMixin(object):
    # A class for getting object    
    model = Plate
    #lookup = 'plate_id'
    
    def get_object(self):
        #plate_id = self.kwargs.get(self.lookup)
        plate_id = self.kwargs.get("plate_id")
        instance = None
        if plate_id is not None:
            instance = get_object_or_404(self.model, plate_id=plate_id)
        return instance

class PlatePageView(PlateObjectMixin, UpdateView):
    # A class for Plate Update View
    template_name = "main/coba.html"

    list_field = (
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
            
    def get(self, request, plate_id=None, *args, **kwargs):
        # GET Method
        instance = self.get_object()

        if instance is not None:
            form = PlateUpdateForm(instance=instance)
            ObjectUpdateFormSet = inlineformset_factory(Plate, StarObject, 
            form=ObjectUpdateForm, extra=0, can_delete=False)
            images = Plate.objects.get(plate_id=plate_id)
            
            formset = ObjectUpdateFormSet(instance=images)
            
            context = {
                'images': images,
                'form': form,
                "formset": formset,
            }
            
        return render(request=request, 
        template_name=self.template_name,
        context=context)

    def post(self, request, plate_id=None, *args, **kwargs):
        # POST Method
        instance = self.get_object()

        if instance is not None:          
            form = PlateUpdateForm(request.POST, instance=instance)
            #ObjectFormSet = inlineformset_factory(Plate, StarObject, fields=(self.fields), extra=0)
            ObjectUpdateFormSet = inlineformset_factory(Plate, StarObject, form=ObjectUpdateForm, extra=0, can_delete=False)
            formset = ObjectUpdateFormSet(request.POST, queryset=StarObject.objects.all(), instance=instance)             
                   
            if form.is_valid() and formset.is_valid():
                form.save()
                formset.save()
                return redirect('platelist')

            context = {
                'form': form,
                "formset": formset,
            }
            print('instance:', instance)
            print('context:', context)
        return render(request=request, 
        template_name=self.template_name,
        context=context)
