# Generated by Django 3.2.9 on 2022-05-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerJob', '0028_delete_presencialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presencialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trabajo', models.CharField(max_length=30)),
            ],
        ),
    ]
