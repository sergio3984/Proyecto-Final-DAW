# Generated by Django 3.2.9 on 2022-05-15 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerJob', '0034_ofertaempleo_puesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertaempleo',
            name='Contrato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seekerJob.tipocontrato'),
        ),
    ]