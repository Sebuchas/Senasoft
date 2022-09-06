import django import forms
from .models import Page

class ClienteForm(forms.ModelFrom):
    class Meta:
        model=Page
        fields=['']