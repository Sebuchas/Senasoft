from django.db import models
from django.utils.translation import gettext_lazy as _ 
from Sondeo.models import *
from django.contrib.auth.models import User

class T_documento(models.TextChoices):
    CC = 'CC',_('Cédula de ciudadanía')
    TI = 'TI',_('Tarjeta de Identidad')
    CE = 'CE',_('Cédula de Extranjería')
class Sexo(models.TextChoices):
    M = 'M',_('Hombre') 
    F = 'F',_('Mujer')
    IS = 'IS',_('Intersexual')
    I = 'I',_('Indefinido')
    PD = 'PD',_('Prefieren no decir')
class Discapacidad(models.TextChoices):
    A = 'A',_('Auditiva')
    V = 'V',_('Visual')
    C = 'C',_('Cognitiva')
    F = 'F',_('Física')
    O = 'O',_('Otra')
    NA = 'NA',_('No aplica')
class Estrato(models.TextChoices):
    A = 'A',_('A')
    B = 'B',_('B')
    C = 'C',_('C')
    D = 'D',_('D')
class N_educativo(models.TextChoices):
    PA = 'PA',_('Primaria')
    B = 'B',_('Bachiller')
    T = 'T',_('Técnico')
    TG = 'TG',_('Tecnolólogo')
    P = 'P',_('Profesional')
class T_afiliacion(models.TextChoices):
    S = 'S',_('Subsidiado')
    C = 'C',_('Contributivo')
class SiNo(models.TextChoices):
    SI = 'SI',_('Sí')
    NO = 'NO',_('No')
class Dispositivos(models.TextChoices):
    TM = 'TM',_('T. Móvil')
    C = 'C',_('Computador')
    T = 'T',_('Tablet')
    OC = 'OC',_('Otro ¿Cuál?')
# ----------------------------------------------------------

class Ciudadano(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Id_Staff')
    nombre = models.CharField(max_length=250, verbose_name=u"Nombres Completos", db_column=u"nombresCompletos")
    apellido = models.CharField(max_length=100, verbose_name=u"Apellidos", db_column=u"apellidos")
    t_doc = models.CharField(max_length=2, db_column=u"tDocumento", verbose_name="Tipo de Documento", choices=T_documento.choices)
    no_documento = models.CharField(max_length=10, verbose_name=u"Número de documento", db_column=u"nDocumento")
    sexo = models.CharField(max_length=2, db_column=u"sexo", choices=Sexo.choices)
    telefono_c = models.CharField(max_length=10, verbose_name=u"Teléfono Celular", null=True, blank=True, db_column=u"tCelular")
    telefono_f = models.CharField(max_length=10, verbose_name=u"Teléfono Fijo", null=True, blank=True, db_column=u"tFijo")
    correo = models.EmailField(verbose_name=u"Correo Electrónico", max_length=254, db_column=u"correo")
    departamento = models.CharField(verbose_name=u"Departamento", db_column=u"departamento", max_length=80)
    municipio = models.CharField(verbose_name=u"Municipio", db_column=u"municipio", max_length=80)
    direccion = models.CharField(verbose_name=u"Dirección", db_column=u"dirección", max_length=150, null=True, blank=True,)
    barrio = models.CharField(verbose_name=u"Barrio/Vereda", db_column=u"barrio", max_length=80)
    f_nacimiento = models.DateField(verbose_name=u"Fecha de Nacimiento", db_column=u"fNacimiento")
    etnia = models.CharField(max_length=50, db_column=u"etnia")
    discapacidad = models.CharField(max_length=2, db_column=u"discapacidad", choices=Discapacidad.choices)
    estrato = models.CharField(max_length=2, db_column=u"estrato", choices=Estrato.choices)
    n_educativo = models.CharField(max_length=2, db_column=u"nEducativo", choices=N_educativo.choices)
    d_tecnologicos = models.CharField(max_length=2, db_column=u"dTecnologicos", choices=SiNo.choices)
    dispositivos = models.CharField(max_length=2, db_column=u"dispositivos", choices=Dispositivos.choices)
    conectividad = models.CharField(max_length=2, db_column=u"conectividad", choices=SiNo.choices, null=True, blank=True)
    t_afiliacion = models.CharField(max_length=2, db_column=u"afiliacion", choices=T_afiliacion.choices, null=True, blank=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre +" "+ self.apellido
    def clean(self):
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()

