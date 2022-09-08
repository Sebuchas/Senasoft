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

class SondeoForm(forms.ModelForm):
    class Meta:
        model = Sondeo
        fields = {'nombre','idTema','tipo','fechaApertura','fechaCierre','icono'}
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'idTema':forms.Select(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            'fechaApertura': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control fuente',
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
            'fechaCierre': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control fuente',
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),}

class ParametroForm(forms.ModelForm):
    class Meta:
        model = Sondeo
        fields = {'sexo','departamento','municipio','etnia','discapacidad','estrato','n_educativo','d_tecnologicos','dispositivos','conectividad','t_afiliacion'}
        widgets = {
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'departamento': forms.Select(attrs={'class':'form-control'}),
            'municipio': forms.Select(attrs={'class':'form-control'}),
            'etnia': forms.Select(attrs={'class':'form-control'}),
            'discapacidad': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'n_educativo': forms.Select(attrs={'class':'form-control'}),
            'd_tecnologicos': forms.Select(attrs={'class':'form-control'}),
            'dispositivos': forms.Select(attrs={'class':'form-control'}),
            'conectividad': forms.Select(attrs={'class':'form-control'}),
            't_afiliacion': forms.Select(attrs={'class':'form-control'}),
        }