# Generated by Django 3.1.2 on 2020-10-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEncuesta', '0009_report_fallo'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='contador',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='fallo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]