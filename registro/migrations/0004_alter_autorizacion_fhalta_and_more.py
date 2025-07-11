# Generated by Django 5.1.5 on 2025-02-13 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_alter_autorizacion_fhalta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 2, 13, 11, 48, 41, 382834, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='autorizacion',
            name='FHAutorizacion',
            field=models.DateTimeField(db_column='FHAUTORIZACION', db_default=datetime.datetime(2025, 2, 13, 11, 48, 41, 382809, tzinfo=datetime.timezone.utc), help_text='Fecha y hora del registro de la autorización', verbose_name='Fecha y hora de la autorización'),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 2, 13, 11, 48, 41, 383780, tzinfo=datetime.timezone.utc), verbose_name='Fecha y hora del alta'),
        ),
    ]
