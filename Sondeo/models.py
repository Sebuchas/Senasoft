
from email.policy import default
from pickle import NONE
from turtle import title
from django.db import models
from django.utils.translation import gettext_lazy as _
from Usuario.models import Ciudadano

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
class Tema(models.Model):
    tema = models.CharField(db_column=u"tema", max_length=250)
    def __str__(self):
        return self.tema
    def clean(self):
        self.tema = self.tema.title()
class Sondeo(models.Model):
    idTema=models.ForeignKey(Tema, db_column=u"idTema", on_delete=models.CASCADE, verbose_name=u"Tema")
    class Tipo(models.TextChoices):
        O = 'O',_('Opinión')
        C = 'C',_('Censo')
        OT = 'OT',_('Otro')
    tipo = models.CharField(max_length=15, db_column=u"tipoSondeo", choices=Tipo.choices)
    fechaApertura = models.DateField(db_column=u"fechaApertura", verbose_name=u"Fecha de Apertura")
    fechaCierre = models.DateField(db_column=u"fechaCierre", verbose_name=u"Fecha de Cierre")
    icono = models.ImageField(upload_to="media/", null=False, blank=False, default="media/icon.png")
    estado = models.BooleanField(default=True)

class Parametro(models.Model):
    idSondeo = models.ForeignKey(Sondeo, db_column=u"idSondeo", verbose_name=u"Sondeo", on_delete=models.CASCADE)
    sexo = models.CharField(max_length=2, db_column=u"sexo", choices=Sexo.choices, null=True, blank=True, default=Sexo.PD)
    departamento = models.CharField(verbose_name=u"Departamento", db_column=u"departamento", max_length=80, null=True, blank=True)
    municipio = models.CharField(verbose_name=u"Municipio", db_column=u"municipio", max_length=80, null=True, blank=True)
    barrio = models.CharField(verbose_name=u"Barrio/Vereda", db_column=u"barrio", max_length=80, null=True, blank=True)
    etnia = models.CharField(max_length=50, db_column=u"etnia", null=True, blank=True)
    discapacidad = models.CharField(max_length=2, db_column=u"discapacidad", choices=Discapacidad.choices, null=True, blank=True, default=Discapacidad.NA)
    estrato = models.CharField(max_length=2, db_column=u"estrato", choices=Estrato.choices, null=True, blank=True, default=Estrato.A)
    n_educativo = models.CharField(max_length=2, db_column=u"nEducativo", choices=N_educativo.choices, null=True, blank=True, default=N_educativo.B)
    d_tecnologicos = models.CharField(max_length=2, db_column=u"dTecnologicos", choices=SiNo.choices, null=True, blank=True, default=SiNo.NO)
    dispositivos = models.CharField(max_length=2, db_column=u"dispositivos", choices=Dispositivos.choices, null=True, blank=True, default=Dispositivos.C)
    conectividad = models.CharField(max_length=2, db_column=u"conectividad", choices=SiNo.choices, null=True, blank=True, default=SiNo.NO)
    t_afiliacion = models.CharField(max_length=2, db_column=u"afiliacion", choices=T_afiliacion.choices, null=True, blank=True, default=T_afiliacion.S)

class Certificacion(models.Model):
    idCiudadano=models.ForeignKey(Ciudadano, db_column=u"idCiudadano", verbose_name=u"Ciudadano", on_delete=models.CASCADE)
    idSondeo=models.ForeignKey(Sondeo, db_column=u"idSondeo", verbose_name=u"Sondeo", on_delete=models.CASCADE)
    nombre=models.CharField(max_length=6, db_column=u"nSondeo", verbose_name=u"Nombre Sondeo")
    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    pregunta = models.TextField(db_column=u"pregunta", max_length=254, verbose_name=u"Pregunta")
    idSondeo=models.ForeignKey(Sondeo, db_column=u"idSondeo", on_delete=models.CASCADE)
    def __str__(self):
        return self.pregunta(title)

