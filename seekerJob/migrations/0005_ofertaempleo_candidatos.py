# Generated by Django 3.2.9 on 2022-04-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerJob', '0004_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertaempleo',
            name='Candidatos',
            field=models.ManyToManyField(to='seekerJob.Usuario'),
        ),
    ]
