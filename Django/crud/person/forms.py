
from django import forms
from .models import Person
from . import models
class PersonFrm(forms.ModelForm):
    class  Meta:
        model= Person
        fields='__all__'