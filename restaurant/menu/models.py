from contextlib import nullcontext
from distutils import extension
from distutils.command.upload import upload
import os
from django.db import models
from django.contrib.auth.models import User
import uuid


def generate_img_file_path(instance,filename):
    img_ext=filename.split('.')[-1]
    filename  = f'{instance}_{uuid.uuid4()}.{img_ext}'
    return os.path.join('images/',filename)

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    plate_size=models.PositiveIntegerField()
    discount=models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(blank=True,upload_to=generate_img_file_path)
    date_updated = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


# Create your models here.
