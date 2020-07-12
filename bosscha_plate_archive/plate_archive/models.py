from django.db import models
from django.utils.html import mark_safe

class Plate(models.Model):
    no_plate = models.CharField(max_length=10)
    plate_pic = models.ImageField(blank=True, null=True)
    cover_pic = models.ImageField(blank=True, null=True)
    checked = models.BooleanField(blank=True, default=False)

    def plate_tag(self):
        if self.plate_pic:
            return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.plate_pic))
        else:
            return mark_safe('<span>Please upload the image</span>')

    def cover_tag(self):
        if self.cover_pic:
            return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.cover_pic))
        else:
            return mark_safe('<span>Please upload the image</span>')

    plate_tag.short_description = 'Plate Image'
    cover_tag.short_description = 'Cover Image'

    def __str__(self):
        return self.no_plate

class StarObject(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, related_name='star_object')
    star_object = models.CharField(max_length=20)
    date = models.CharField(max_length=10, default="1970-01-01")
    ra = models.CharField(max_length=20)
    dec = models.FloatField()
    dec_obs = models.FloatField()
    ha = models.CharField(max_length=20)
    t_start = models.TimeField()
    t_end = models.TimeField()
    exposure = models.CharField(verbose_name="Exposure (seconds)", max_length=20)
    temperature = models.FloatField(null=True, blank=True)
    focus = models.CharField(max_length=20)
    staand_plaat = models.FloatField(null=True, blank=True)
    emulsion = models.CharField(max_length=20, null=True, blank=True)
    emulsion_no = models.CharField(max_length=20, null=True, blank=True)
    film = models.CharField(max_length=20)
    plate_size = models.CharField(max_length=20)
    camera_filter = models.CharField(verbose_name="Filter", max_length=20)
    grating = models.CharField(max_length=20, null=True, blank=True)
    transparency = models.CharField(max_length=20, null=True, blank=True)
    seeing = models.CharField(max_length=20, null=True, blank=True)
    observer = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.star_object

class ScannedLogbook(models.Model):
    pass