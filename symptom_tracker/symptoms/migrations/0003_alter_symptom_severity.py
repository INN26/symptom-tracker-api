# Generated by Django 5.2 on 2025-04-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='severity',
            field=models.IntegerField(),
        ),
    ]
