# Generated by Django 5.1.4 on 2024-12-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('Asignado', 'Asignado'), ('Devuelto', 'Devuelto')], default='Asignado', max_length=50),
        ),
    ]
