# Generated by Django 3.1.2 on 2020-11-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEncuesta', '0013_remove_reportuser_perfilenc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportuser',
            name='tiempo',
            field=models.TimeField(null=True),
        ),
    ]
