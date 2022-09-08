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
        fields = {'nombre','tipo','fechaApertura','fechaCierre','icono','sexo','etnia','discapacidad',
                  'estrato','n_educativo','d_tecnologicos','dispositivos','conectividad','t_afiliacion'}
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
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
                      }),
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'etnia': forms.Select(attrs={'class':'form-control'}),
            'discapacidad': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'n_educativo': forms.Select(attrs={'class':'form-control'}),
            'd_tecnologicos': forms.Select(attrs={'class':'form-control'}),
            'dispositivos': forms.Select(attrs={'class':'form-control'}),
            'conectividad': forms.Select(attrs={'class':'form-control'}),
            't_afiliacion': forms.Select(attrs={'class':'form-control'}),
            }
            

class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'
        widgets = {
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'etnia': forms.Select(attrs={'class':'form-control'}),
            'discapacidad': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'n_educativo': forms.Select(attrs={'class':'form-control'}),
            'd_tecnologicos': forms.Select(attrs={'class':'form-control'}),
            'dispositivos': forms.Select(attrs={'class':'form-control'}),
            'conectividad': forms.Select(attrs={'class':'form-control'}),
            't_afiliacion': forms.Select(attrs={'class':'form-control'}),
        }
        
