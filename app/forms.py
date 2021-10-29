from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Resume_model

class Resume_form(forms.ModelForm):
    class Meta:
        model = Resume_model 
        fields = "__all__"
