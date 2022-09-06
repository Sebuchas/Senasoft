# Generated by Django 4.1.1 on 2022-09-06 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sondeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(db_column='temaSondeo', max_length=50)),
                ('tipo', models.CharField(choices=[('O', 'Opinión'), ('C', 'Censo'), ('OT', 'Otros')], db_column='tipoSondeo', max_length=15)),
                ('fechaApertura', models.DateField(auto_now=True, db_column='fechaApertura')),
                ('fechaCierre', models.DateField(db_column='fechaCierre')),
                ('icono', models.FileField(db_column='iconos', default=b'N', upload_to='icons/')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField(db_column='pregunta')),
                ('idSondeo', models.ForeignKey(db_column='idSondeo', on_delete=django.db.models.deletion.CASCADE, to='Sondeo.sondeo')),
            ],
        ),
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nSondeo', max_length=6, verbose_name='Nombre Sondeo')),
                ('idCiudadano', models.ForeignKey(db_column='idCiudadano', on_delete=django.db.models.deletion.CASCADE, to='Usuario.ciudadano', verbose_name='Ciudadano')),
                ('idSondeo', models.ForeignKey(db_column='idSondeo', on_delete=django.db.models.deletion.CASCADE, to='Sondeo.sondeo', verbose_name='Sondeo')),
            ],
        ),
    ]
