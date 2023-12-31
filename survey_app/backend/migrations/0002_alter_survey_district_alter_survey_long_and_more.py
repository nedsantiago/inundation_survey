# Generated by Django 4.2.7 on 2023-12-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
