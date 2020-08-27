import os
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from bosscha_plate_archive.settings_base import BASE_DIR
from django.utils.text import slugify
from model_utils import Choices
from model_utils.fields import StatusField, MonitorField


class Plate(models.Model):
    STATUS = Choices(
        ('Unavailable', 'Unavailable'),
        ('Available', 'Available'),
        ('Processed', 'Processed'),
    )

    plate_id = models.CharField(max_length=10)
    cover_id = models.CharField(max_length=10, blank=True, null=True)
    cover_object = models.CharField(verbose_name="Cover Object", max_length=20, null=True, blank=True)
    cover_ra = models.CharField(verbose_name="Cover RA (hh mm)", max_length=20, null=True, blank=True)
    cover_dec = models.FloatField(verbose_name="Cover dec (degree)", null=True, blank=True)
    cover_t_start = models.CharField(verbose_name="Cover T_start", max_length=10, null=True, blank=True)
    cover_t_end = models.CharField(verbose_name="Cover T_end", max_length=10, null=True, blank=True)
    cover_exp = models.CharField(verbose_name="Cover exposure (seconds)", max_length=20, null=True, blank=True)
    cover_emul = models.CharField(verbose_name="Cover emulsion", max_length=20, null=True, blank=True)
    cover_filter = models.CharField(verbose_name="Cover filter", max_length=20, null=True, blank=True)
    cover_grat = models.CharField(verbose_name="Cover grating", max_length=20, null=True, blank=True)
    cover_date = models.CharField(verbose_name="Cover date", max_length=10, null=True, blank=True)
    cover_prog = models.CharField(verbose_name="Cover program", max_length=20, default="Double Star", null=True, blank=True)
    cover_obs = models.CharField(verbose_name="Cover observer", max_length=30, null=True, blank=True)
    meas_auth = models.CharField(verbose_name="Measurement officer", max_length=10, blank=True, null=True)
    meas_date = models.CharField(verbose_name="Measurement date", max_length=10, default="1970-01-01", null=True, blank=True)
    plate_qual = models.CharField(verbose_name="Plate Quality", max_length=10, null=True, blank=True)
    cover_note = models.TextField(verbose_name="Cover remarks", null=True, blank=True)
    cover_pic = models.ImageField(blank=True, null=True)
    plate_pic = models.ImageField(blank=True, null=True)
    preview_pic = models.ImageField(blank=True, null=True)
    logbook_pic = models.FileField(blank=True, null=True)
    status = StatusField(max_length=100, choices=STATUS, default=STATUS.Unavailable)
    date_modified = MonitorField(monitor='status', when=['Processed'])
    checked = models.BooleanField(blank=True, default=False)

    def cover_tag(self):
        cover_path = os.path.join(BASE_DIR, 'media', 'plate', str(self.plate_id), str(self.cover_pic))
        if os.path.exists(cover_path):
            #self.status = 'Available'
            return mark_safe('<a href="/media/plate/%s/%s" target="_blank">%s</a>' % (self.plate_id, self.cover_pic, self.cover_pic))
        else:
            return mark_safe(self.cover_pic)
            
    def plate_tag(self):
        plate_path = os.path.join(BASE_DIR, 'media', 'plate', str(self.plate_id), str(self.plate_pic))
        if os.path.exists(plate_path):
            #self.status = 'Available'
            return mark_safe('<a href="/media/plate/%s/%s" target="_blank">%s</a>' % (self.plate_id, self.plate_pic, self.plate_pic))
        else:
            return mark_safe(self.plate_pic)
           
    def preview_tag(self):
        preview_path = os.path.join(BASE_DIR, 'media', 'plate', str(self.plate_id), str(self.preview_pic))
        if os.path.exists(preview_path):
            #self.status = 'Available'
            return mark_safe('<a href="/media/plate/%s/%s" target="_blank">%s</a>' % (self.plate_id, self.preview_pic, self.preview_pic))
        else:
            return mark_safe(self.preview_pic)

    def logbook_tag(self):
        logbook_path = os.path.join(BASE_DIR, 'media', 'logbook', str(self.logbook_pic))
        if os.path.exists(logbook_path):
            return mark_safe('<a href="/media/logbook/%s" target="_blank">%s</a>' % (self.logbook_pic, self.logbook_pic))
        else:
            return mark_safe(self.logbook_pic)
    
    cover_tag.short_description = 'Cover Image'
    plate_tag.short_description = 'Plate Image'
    preview_tag.short_description = 'Preview Image'
    logbook_tag.short_description = 'Logbook Image'
        
    def get_absolute_url(self):
        return reverse("platepage", kwargs={"plate_id": self.plate_id})

    class Meta:
        ordering = ('status',)

    @property
    def CoverURL(self):
        try:
            url = self.cover_tag.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.plate_id

class StarObject(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, related_name='star_object', null=True, blank=True)
    star_object = models.CharField(max_length=20)
    date = models.CharField(max_length=10, default="1970-01-01", null=True, blank=True)
    ra = models.CharField(max_length=20, null=True, blank=True)
    dec = models.FloatField(verbose_name="Declination (degree)", null=True, blank=True)
    dec_obs = models.FloatField(verbose_name="Observed declination (degree)", null=True, blank=True)
    ha = models.CharField(max_length=20, null=True, blank=True)
    t_start = models.CharField(max_length=10, null=True, blank=True)
    t_end = models.CharField(max_length=10, null=True, blank=True)
    exposure = models.CharField(verbose_name="Exposure (seconds)", max_length=20, null=True, blank=True)
    temperature = models.FloatField(verbose_name="Temperature (Celcius)", null=True, blank=True)
    focus = models.CharField(verbose_name="Focus (mm)", max_length=20, null=True, blank=True)
    staand_plaat = models.FloatField(verbose_name="Plate Stand (degree)", null=True, blank=True)
    emulsion = models.CharField(max_length=20, null=True, blank=True)
    emulsion_no = models.CharField(max_length=20, null=True, blank=True)
    film = models.CharField(max_length=20, null=True, blank=True)
    plate_size = models.CharField(verbose_name="Plate size (mm x mm)", max_length=20, null=True, blank=True)
    camera_filter = models.CharField(verbose_name="Filter", max_length=20, null=True, blank=True)
    grating = models.CharField(max_length=20, null=True, blank=True)
    transparency = models.CharField(max_length=20, null=True, blank=True)
    seeing = models.CharField(max_length=20, null=True, blank=True)
    observer = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.star_object