# Generated by Django 5.1.5 on 2025-05-04 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminusr', '0011_alter_usuario_fhalta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='FHAlta',
            field=models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 5, 4, 2, 33, 57, 365169, tzinfo=datetime.timezone.utc)),
        ),
    ]
