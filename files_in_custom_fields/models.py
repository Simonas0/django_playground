import os

from django import forms
from django.core.files.storage import FileSystemStorage
from django.db import models

from django_playground.settings import MEDIA_ROOT

from .widgets import MultiWidget

# Create your models here.


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(MEDIA_ROOT, name))
        return name


def file_path(instance, filename):
    return os.path.join(
        "{}{}".format(instance.id, os.path.splitext(filename)[1])
    )


class Field(forms.Field):
    widget = MultiWidget([forms.TextInput(), forms.FileInput()])


class MyType(models.Field):
    name_in_field = models.CharField(max_length=100)
    file_in_field = models.FileField(upload_to=file_path, storage=OverwriteStorage())

    def db_type(self, connection):
        return "custom_field"

    def formfield(self, form_class=None, choices_form_class=None, **kwargs):
        return super().formfield(**{"form_class": Field})

    def save_form_data(self, instance, data):
        # I want attribute to become tuple (CharField, FieldFile)
        # just like it happens with the file outside of MyType
        # but attribute becomes (CharField, TemporaryUploadedFile)
        # what is identical to data and throws error when saving
        # Default behavior:
        setattr(instance, self.name, data)
        # I suppose I should write something like below, but what exactly?
        # setattr(getattr(instance, self.name), "name_in_field", data[0])
        # setattr(getattr(instance, self.name), "file_in_field", data[1])


class Model(models.Model):
    file = models.FileField(upload_to=file_path, storage=OverwriteStorage())
    field = MyType()
