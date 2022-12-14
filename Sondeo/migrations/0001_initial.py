# Generated by Django 4.1.1 on 2022-09-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(db_column='tema', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sondeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254, verbose_name='Nombre del Sondeo')),
                ('tipo', models.CharField(choices=[('O', 'Opinión'), ('C', 'Censo'), ('OT', 'Otro')], db_column='tipoSondeo', max_length=15)),
                ('fechaApertura', models.DateField(db_column='fechaApertura', verbose_name='Fecha de Apertura')),
                ('fechaCierre', models.DateField(db_column='fechaCierre', verbose_name='Fecha de Cierre')),
                ('icono', models.ImageField(default='media/icon.png', upload_to='media/')),
                ('estado', models.BooleanField(default=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Hombre'), ('F', 'Mujer'), ('IS', 'Intersexual'), ('I', 'Indefinido'), ('PD', 'Prefieren no decir')], db_column='sexo', default='PD', max_length=2, null=True)),
                ('departamento', models.CharField(blank=True, db_column='departamento', max_length=80, null=True, verbose_name='Departamento')),
                ('municipio', models.CharField(blank=True, db_column='municipio', max_length=80, null=True, verbose_name='Municipio')),
                ('barrio', models.CharField(blank=True, db_column='barrio', max_length=80, null=True, verbose_name='Barrio/Vereda')),
                ('etnia', models.CharField(blank=True, db_column='etnia', max_length=50, null=True)),
                ('discapacidad', models.CharField(blank=True, choices=[('A', 'Auditiva'), ('V', 'Visual'), ('C', 'Cognitiva'), ('F', 'Física'), ('O', 'Otra'), ('NA', 'No aplica')], db_column='discapacidad', default='NA', max_length=2, null=True)),
                ('estrato', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], db_column='estrato', default='A', max_length=2, null=True)),
                ('n_educativo', models.CharField(blank=True, choices=[('PA', 'Primaria'), ('B', 'Bachiller'), ('T', 'Técnico'), ('TG', 'Tecnolólogo'), ('P', 'Profesional')], db_column='nEducativo', default='B', max_length=2, null=True)),
                ('d_tecnologicos', models.CharField(blank=True, choices=[('SI', 'Sí'), ('NO', 'No')], db_column='dTecnologicos', default='NO', max_length=2, null=True)),
                ('dispositivos', models.CharField(blank=True, choices=[('TM', 'T. Móvil'), ('C', 'Computador'), ('T', 'Tablet'), ('OC', 'Otro ¿Cuál?')], db_column='dispositivos', default='C', max_length=2, null=True)),
                ('conectividad', models.CharField(blank=True, choices=[('SI', 'Sí'), ('NO', 'No')], db_column='conectividad', default='NO', max_length=2, null=True)),
                ('t_afiliacion', models.CharField(blank=True, choices=[('S', 'Subsidiado'), ('C', 'Contributivo')], db_column='afiliacion', default='S', max_length=2, null=True)),
                ('idTema', models.ForeignKey(db_column='idTema', on_delete=django.db.models.deletion.CASCADE, to='Sondeo.tema', verbose_name='Tema')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField(db_column='pregunta', max_length=254, verbose_name='Pregunta')),
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
