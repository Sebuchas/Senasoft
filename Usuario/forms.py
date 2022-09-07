from django import forms
from Usuario.models import *

class CiudadanoForm(forms.ModelForm):
    class Meta:
        model = Ciudadano
        fields = ['nombre','apellido','t_doc','no_documento','sexo',
                'telefono_c','telefono_f','correo',
                'departamento','municipio','direccion',
                'barrio','f_nacimiento','etnia','discapacidad',
                'estrato','n_educativo','d_tecnologicos',
                'dispositivos','conectividad','t_afiliacion']
        widgets = {
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'no_documento': forms.NumberInput(attrs={'class':'form-control'}),
            'telefono_f': forms.NumberInput(attrs={'class':'form-control'}),
            'telefono_c': forms.NumberInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'departamento': forms.SelectMultiple(attrs={'class':'form-control'}),
            'municipio': forms.SelectMultiple(attrs={'class':'form-control'}),
            'f_nacimiento': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
            'etnia': forms.Select(attrs={'class':'form-control'}),
            'discapacidad': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'n_educativo': forms.Select(attrs={'class':'form-control'}),
            'd_tecnologicos': forms.Select(attrs={'class':'form-control'}),
            'dispositivos': forms.Select(attrs={'class':'form-control'}),
            'conectividad': forms.Select(attrs={'class':'form-control'}),
            't_afiliacion': forms.Select(attrs={'class':'form-control'}),
        }

