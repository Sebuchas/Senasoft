
from pickle import NONE
from django.db import models
from django.utils.translation import gettext_lazy as _
from Usuario.models import Ciudadano

class Sondeo(models.Model):
    tema = models.CharField(max_length=50, db_column=u"temaSondeo")
    class Tipo(models.TextChoices):
        O = 'O',_('Opinión')
        C = 'C',_('Censo')
        OT = 'OT',_('Otros')
    tipo = models.CharField(max_length=15, db_column=u"tipoSondeo", choices=Tipo.choices)
    fechaApertura = models.DateField(auto_now=True, db_column=u"fechaApertura")
    fechaCierre = models.DateField(db_column=u"fechaCierre")
    icono = models.FileField(upload_to='icons/', db_column=u"iconos", default=NONE)
    estado = models.BooleanField(default=True)
    
class Certificacion(models.Model):
    idCiudadano=models.ForeignKey(Ciudadano, db_column=u"idCiudadano", verbose_name=u"Ciudadano", on_delete=models.CASCADE)
    idSondeo=models.ForeignKey(Sondeo, db_column=u"idSondeo", verbose_name=u"Sondeo", on_delete=models.CASCADE)
    nombre=models.CharField(max_length=6, db_column=u"nSondeo", verbose_name=u"Nombre Sondeo")
    
class Preguntas(models.Model):
    pregunta = models.TextField(db_column=u"pregunta")
    idSondeo=models.ForeignKey(Sondeo, db_column=u"idSondeo", on_delete=models.CASCADE)