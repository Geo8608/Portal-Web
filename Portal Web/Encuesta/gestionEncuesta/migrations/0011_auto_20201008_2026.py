# Generated by Django 3.1.2 on 2020-10-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEncuesta', '0010_auto_20201008_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='contador',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='fallo',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]