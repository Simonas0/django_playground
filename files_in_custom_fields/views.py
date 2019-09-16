from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ModelForm

# Create your views here.


def new(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        form = ModelForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse("files_in_custom_fields:new"))
    return render(request, "files_in_custom_fields/new.html", {"form": ModelForm()})
