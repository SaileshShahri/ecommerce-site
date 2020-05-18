import datetime 
import random 
import os 


from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL
# Create your models here.

def get_filename(path):
    return os.path.basename(path)

def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "categoryimg/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.name