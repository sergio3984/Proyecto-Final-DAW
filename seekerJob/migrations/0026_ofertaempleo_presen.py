# Generated by Django 3.2.9 on 2022-05-13 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerJob', '0025_remove_ofertaempleo_presen'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertaempleo',
            name='Presen',
            field=models.ForeignKey( null=True, on_delete=django.db.models.deletion.CASCADE, to='seekerJob.presencialidad'),
        ),
    ]