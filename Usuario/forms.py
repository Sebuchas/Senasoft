from tkinter import Widget
import django import forms
from Usuario.models import *

class CiudadanoForm(forms.ModelFrom):
    class Meta:
        model=Ciudadano
        fields=['']
        widgets = {
            
        }