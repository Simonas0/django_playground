from django import forms

from .models import Model
from .widgets import MultiWidget


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = "__all__"
        widgets = {"field": MultiWidget([forms.TextInput(), forms.FileInput()])}
