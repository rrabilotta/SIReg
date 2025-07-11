# Generated by Django 5.1.5 on 2025-05-04 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_c_tipo_acto_inmobiliario_vigente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_tipo_acto_no_inmobiliario',
            fields=[
                ('IdTipoActo', models.SmallAutoField(db_column='IDTIPOACTO', db_comment='Identificador único', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('NombreActo', models.CharField(db_column='NOMBRE', db_comment='Nombre del acto', max_length=50, unique=True)),
                ('Tabla', models.CharField(db_column='TABLA', db_comment='Tabla', db_index=True, max_length=50)),
                ('Llave', models.CharField(db_column='LLAVEPRIMARIA', db_comment='Llave primaria', max_length=50)),
                ('TipoCampoLlave', models.SmallIntegerField(choices=[(0, 'Sin definir'), (1, 'Int'), (2, 'Text'), (3, 'Date'), (4, 'Date-time'), (5, 'URL'), (6, 'Email'), (7, 'Currency'), (8, 'Geometry'), (9, 'Name-field'), (10, 'Password-field')], db_column='TIPOCAMPO', db_comment='Tipo de campo', db_default=0)),
                ('Vigente', models.BooleanField(db_column='Vigencia', db_comment='Vigencia', db_default=False)),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', db_comment='Fecha y hora de alta')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', db_comment='Fecha y hora de modificación')),
            ],
            options={
                'verbose_name_plural': 'Catálogo tipos de actos',
                'ordering': ('NombreActo', 'IdTipoActo', 'Tabla', 'Llave'),
            },
        ),
        migrations.AlterField(
            model_name='autorizacion',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 5, 4, 2, 33, 57, 366918, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='autorizacion',
            name='FHAutorizacion',
            field=models.DateTimeField(db_column='FHAUTORIZACION', db_default=datetime.datetime(2025, 5, 4, 2, 33, 57, 366893, tzinfo=datetime.timezone.utc), help_text='Fecha y hora del registro de la autorización', verbose_name='Fecha y hora de la autorización'),
        ),
        migrations.AlterField(
            model_name='folio_inmobiliario',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', db_default=datetime.datetime(2025, 5, 4, 2, 33, 57, 371076, tzinfo=datetime.timezone.utc), verbose_name='Fecha y hora alta del registro'),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 5, 4, 2, 33, 57, 367820, tzinfo=datetime.timezone.utc), verbose_name='Fecha y hora del alta'),
        ),
        migrations.AlterField(
            model_name='lista_negra_folios_inmobiliarios',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', db_default=datetime.datetime(2025, 5, 4, 2, 33, 57, 378789, tzinfo=datetime.timezone.utc), help_text='Fecha y hora de la incorporación', verbose_name='Fecha y hora incorporación'),
        ),
        migrations.AlterField(
            model_name='lista_negra_folios_no_inmobiliarios',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', db_default=datetime.datetime(2025, 5, 4, 2, 33, 57, 378944, tzinfo=datetime.timezone.utc), help_text='Fecha y hora de la incorporación', verbose_name='Fecha y hora incorporación'),
        ),
    ]
