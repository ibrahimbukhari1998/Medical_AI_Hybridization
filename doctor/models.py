from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Tempstorage(models.Model):
    image = models.ImageField(upload_to = "temp/", null=True, blank=True, validators=[FileExtensionValidator( ['jpg', 'jpeg', 'png'] ) ])
    