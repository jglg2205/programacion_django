# Generated by Django 4.2 on 2023-04-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('contraseña_usuario', models.CharField(max_length=8)),
                ('updated_usuraio', models.DateTimeField(auto_now=True)),
                ('created_usuario', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
