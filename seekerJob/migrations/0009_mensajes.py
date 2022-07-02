# Generated by Django 3.2.9 on 2022-04-30 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seekerJob', '0008_alter_ofertaempleo_candidatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_del_mensaje', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]