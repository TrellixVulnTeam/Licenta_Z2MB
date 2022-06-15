# Generated by Django 4.0.4 on 2022-05-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detections',
            name='mark',
            field=models.CharField(choices=[('isNotMarked', 'Not marked'), ('isDanger', 'Danger'), ('isSafe', 'Safe')], default='Not marked', max_length=20),
        ),
    ]