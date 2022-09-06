from django import forms
from Sondeo.models import *

class TemaForm(forms.ModelForm):
    class Meta:
        model=Tema
        fields = '__all__'

class PreguntaForm(forms.ModelForm):
    class Meta:
        model=Pregunta
        fields = '__all__'