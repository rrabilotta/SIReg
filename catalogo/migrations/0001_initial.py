# Generated by Django 5.1.5 on 2025-02-08 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='c_clase_documento',
            fields=[
                ('IdClaseDocumento', models.AutoField(db_column='IDCLASEDOC', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=50, unique=True)),
                ('Descripcion', models.TextField(db_column='DESCRIPCION')),
                ('Oficial', models.BooleanField(db_column='OFICIAL', db_default=False)),
                ('Expira', models.BooleanField(db_column='EXPIRA', db_default=True)),
            ],
            options={
                'verbose_name_plural': 'Catálogo de clase de documentos',
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='c_clase_reporte',
            fields=[
                ('IdClaseReporte', models.AutoField(db_column='IDTIPOCONSTANCIA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=50, unique=True, verbose_name='Clase de reporte')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de clases de reportes',
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='c_entidad',
            fields=[
                ('CveGeograficaEntidad', models.CharField(db_column='CVEGEOGRAFICA', db_index=True, help_text='Clave geográfica INEGI de la entidad', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Clave geográfica')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre de la entidad', max_length=100, verbose_name='Entidad')),
                ('ClaveEntidad', models.CharField(db_column='CVEENTIDAD', help_text='Clave INEGI de la entidad', max_length=2, null=True, verbose_name='Clave de la entidad')),
            ],
            options={
                'verbose_name_plural': 'Entidades (estados, provincias o departamentos)',
                'ordering': ('CveGeograficaEntidad', 'Nombre'),
            },
        ),
        migrations.CreateModel(
            name='c_moneda',
            fields=[
                ('CveMoneda', models.CharField(db_column='CVEMONEDA', db_index=True, max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Clave ISO de la moneda')),
                ('Moneda', models.CharField(db_column='NOMMONEDA', db_index=True, max_length=50, verbose_name='Moneda')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de monedas',
                'ordering': ('Moneda',),
            },
        ),
        migrations.CreateModel(
            name='c_nombre_vialidad',
            fields=[
                ('IdNombreVialidad', models.BigAutoField(db_column='IDNOMVIALIDAD', db_index=True, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(db_column='NOMBRE', db_default='Calle', db_index=True, max_length=100)),
                ('Aliases', models.JSONField(db_column='ALIASES', db_default='', help_text='Aliases (viariantes) en JSON del nombre', verbose_name='Aliases')),
            ],
            options={
                'verbose_name_plural': 'Nombres de vialidades (Calles, avenidas, callejones, etc.)',
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='c_regimen_fiscal',
            fields=[
                ('IdRegimenFiscal', models.BigAutoField(db_column='IDREGIMENFISCAL', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('ClaveSAT', models.IntegerField(db_column='CVESAT', db_default=0, db_index=True, help_text='Clave SAT del régimen fiscal', verbose_name='Clave SAT')),
                ('Nombre', models.CharField(db_column='NOMBRE', help_text='Régimen fiscal', max_length=50, unique=True, verbose_name='Régimen fiscal')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción del régime fiscal', verbose_name='Descripción')),
                ('PersonaMoral', models.BooleanField(db_column='PERSONAMORAL', db_default=False, help_text='Selecciónelo si es aplicable a una persona moral o jurídica', verbose_name='Aplica a persona moral')),
                ('Vigente', models.BooleanField(db_column='VIGENTE', default=False, help_text='Selecciónelo si es un régimen fiscal vigente', verbose_name='Está vigente')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de regímenes fiscales',
                'ordering': ('Nombre', 'Descripcion', 'PersonaMoral'),
            },
        ),
        migrations.CreateModel(
            name='c_tipo_documento_identidad',
            fields=[
                ('IdTipoDocumentoIdentidad', models.AutoField(db_column='IDTIPODOCIDENT', db_index=True, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(db_column='NOMBRE', db_default='Credencial de ...', max_length=100, unique=True, verbose_name='Tipo de documento')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
                ('Expira', models.BooleanField(db_column='DOCEXPIRA', default=True, verbose_name='¿El documento expira?')),
            ],
            options={
                'verbose_name_plural': 'Tipos de documentos de identidad',
                'ordering': ('Nombre', 'Expira'),
            },
        ),
        migrations.CreateModel(
            name='c_tipo_recibo',
            fields=[
                ('IdTipoRecibo', models.AutoField(db_column='IDTIPORECIBO', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=50, unique=True, verbose_name='Tipo de recibo')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Tipos de recibos',
                'ordering': ('Nombre', 'Descripcion'),
            },
        ),
        migrations.CreateModel(
            name='c_uso_cdfi',
            fields=[
                ('IdUsoCDFI', models.BigAutoField(db_column='IDUSOCDFI', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('ClaveSAT', models.CharField(db_column='CVESAT', db_default='', help_text='Clave SAT del régimen fiscal', max_length=5, verbose_name='Clave SAT')),
                ('Nombre', models.CharField(db_column='NOMBRE', help_text='Uso del certificado digital fiscal', max_length=100, unique=True, verbose_name='Uso del CDFI')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción', null=True, verbose_name='Descripción')),
                ('PersonaMoral', models.BooleanField(db_column='PERSONAMORAL', db_default=False, help_text='Aplicable a personas morales o jurídicas', verbose_name='Perosna moral')),
                ('PersonaFisica', models.BooleanField(db_column='PERSONAFISICA', db_default=False, help_text='Aplicable a personas físicas', verbose_name='Perosna física')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de usos de los CDFI',
                'ordering': ('ClaveSAT', 'Nombre', 'PersonaMoral'),
            },
        ),
        migrations.CreateModel(
            name='c_municipio',
            fields=[
                ('CveGeograficaMunicipio', models.CharField(db_column='CVEGEOGRAFICA', db_index=True, help_text='Clave geográfica INEGI del municipio', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Clave geográfica')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre del municipio', max_length=100, verbose_name='Municipio')),
                ('ClaveMunicipio', models.CharField(db_column='CVEMUNICIPIO', help_text='Clave INEGI del municipio respecto a la entidad', max_length=3, null=True, verbose_name='Clave del Municipio')),
                ('ClaveGeogEntidad', models.ForeignKey(db_column='CVEGEOENTIDAD', db_constraint=False, help_text='Entidad', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_entidad', verbose_name='Entidad')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'ordering': ('CveGeograficaMunicipio', 'Nombre'),
            },
        ),
        migrations.CreateModel(
            name='c_localidad',
            fields=[
                ('CveGeograficaLocalidad', models.CharField(db_column='CVEGEOGRAFICA', db_default='', db_index=True, help_text='Clave geográfica INEGI de la localidad', max_length=20, primary_key=True, serialize=False, verbose_name='Clave geográfica')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_default='LOCALIDAD', db_index=True, help_text='Nombre de la localidad', max_length=100, verbose_name='Localidad')),
                ('ClaveLocalidad', models.CharField(db_column='CVELOCALIDAD', help_text='Clave INEGI  de la localidad respecto al municipio', max_length=4, null=True, verbose_name='Clave de la localidad')),
                ('ClaveGeogMunicipio', models.ForeignKey(db_column='CVEGEOMUNICIPIO', db_constraint=False, help_text='Municipio y entidad', on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
                'ordering': ('CveGeograficaLocalidad', 'Nombre'),
                'unique_together': {('CveGeograficaLocalidad', 'Nombre')},
            },
        ),
        migrations.CreateModel(
            name='c_pais',
            fields=[
                ('CvePais', models.CharField(db_column='CVEPAIS', db_index=True, help_text='Clave ISO (tres posiciones) del país', max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Clave ISO')),
                ('Nombre', models.CharField(db_column='NOMBRE', help_text='Nombre del país', max_length=100, verbose_name='País')),
                ('CodigoTelefonico', models.CharField(db_column='CODIGOTEL', help_text='Código telefónico', max_length=10, verbose_name='Código telefónico')),
                ('Continente', models.CharField(db_column='CONTINENTE', help_text='Continente', max_length=15, null=True, verbose_name='Continente')),
                ('Moneda', models.ForeignKey(db_column='CVEMONEDA', help_text='Moneda de curso legal', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_moneda', verbose_name='Moneda')),
            ],
            options={
                'verbose_name_plural': 'Países',
                'ordering': ('Nombre', 'CvePais'),
            },
        ),
        migrations.AddField(
            model_name='c_entidad',
            name='ClavePais',
            field=models.ForeignKey(db_column='CVEPAIS', db_constraint=False, help_text='País', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_pais', verbose_name='País'),
        ),
        migrations.CreateModel(
            name='c_asentamiento_humano',
            fields=[
                ('ClaveGeograficaAsentamiento', models.CharField(db_column='CVEGEOASENTAMIENTO', db_index=True, help_text='Clave geográfica INEGI del asentamiento', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Clave geográfica')),
                ('Nombre', models.CharField(db_column='ASENTAMIENTO', db_default='', db_index=True, help_text='Nombre del asentamiento (colonia, barrio, pueblo, unidad habitacional, etc.)', max_length=100, verbose_name='Asentamiento')),
                ('CodigoPostal', models.CharField(db_column='CODIGOPOSTAL', db_index=True, help_text='Código postal SEPOMEX', max_length=5, verbose_name='Código postal')),
                ('AutoridadResponsable', models.CharField(db_column='AUTORIDADRESPONSABLE', help_text='Autoridad responsable por el dato', max_length=100, null=True, verbose_name='Atoridad responsable')),
                ('TipoAsentamiento', models.CharField(db_column='TIPOASENTAMIENTO', db_default='COLONIA', help_text='Tipo de asentamiento humano', max_length=50, verbose_name='Tipo')),
                ('FUltimaActualizacion', models.CharField(db_column='ULTIMAACTUALIZACION', help_text='Fecha de la actualización correspondiente (mes/año)', max_length=10, verbose_name='Fecha de la actualización')),
                ('ClaveAsentamiento', models.CharField(db_column='CVEASENTAMIENTO', help_text='Clave INEGI del asentamiento respecto a la localidad', max_length=4, null=True, verbose_name='Clave del asentamiento')),
                ('ClaveGeogLocalidad', models.ForeignKey(db_column='CVEGEOLOCALIDAD', db_constraint=False, help_text='Localidad, municipio y entidad', on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_localidad', verbose_name='Localidad')),
            ],
            options={
                'verbose_name_plural': 'Asentamientos (colonias, barrios, etc.)',
                'ordering': ('CodigoPostal', 'ClaveGeograficaAsentamiento', 'Nombre'),
                'unique_together': {('ClaveGeograficaAsentamiento', 'Nombre', 'CodigoPostal')},
            },
        ),
    ]
