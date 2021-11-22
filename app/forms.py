from django import forms
from django.forms.fields import CharField
from .models import Resume_model
from django.forms import modelformset_factory

ResumeFormSet = modelformset_factory(
    Resume_model, fields="__all__", extra=1
)
