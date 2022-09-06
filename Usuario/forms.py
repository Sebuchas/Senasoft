from django import forms
from Usuario.models import *

class CiudadanoForm(forms.ModelForm):
    class Meta:
        model=Ciudadano
        fields=['nombre','apellido','t_doc','no_documento','sexo',
                'telefono_c','telefono_f','correo',
                'departamento','municipio','direccion',
                'barrio','f_nacimiento','etnia','discapacidad',
                'estrato','n_educativo','d_tecnologicos',
                'dispositivos','conectividad','t_afiliacion']

