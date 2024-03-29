# Generated by Django 4.2 on 2023-05-09 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_autor', models.CharField(max_length=50)),
                ('apellido_autor', models.CharField(max_length=50)),
                ('updated_autor', models.DateTimeField(auto_now=True)),
                ('created_autor', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autor_libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_al', models.DateTimeField(auto_now=True)),
                ('created_al', models.DateTimeField(auto_now_add=True)),
                ('id_autorL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.autor')),
                ('id_libroA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_genero', models.CharField(max_length=100)),
                ('updated_genero', models.DateTimeField(auto_now=True)),
                ('created_genero', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero_libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_gl', models.DateTimeField(auto_now=True)),
                ('created_gl', models.DateTimeField(auto_now_add=True)),
                ('id_generoL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.genero')),
                ('id_libroG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Libro_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_lu', models.DateTimeField(auto_now=True)),
                ('created_lu', models.DateTimeField(auto_now_add=True)),
                ('id_libroU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.libro')),
                ('id_userL', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('puntos', models.CharField(max_length=1)),
                ('updated_valoracion', models.DateTimeField(auto_now=True)),
                ('created_valoracion', models.DateTimeField(auto_now_add=True)),
                ('id_libroV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.libro')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
        migrations.AddField(
            model_name='libro_usuario',
            name='id_valoracionlu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.valoracion'),
        ),
    ]
