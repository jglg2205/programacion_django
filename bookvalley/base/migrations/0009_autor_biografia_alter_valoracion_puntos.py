# Generated by Django 4.2 on 2023-05-31 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_valoracion_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='biografia',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='puntos',
            field=models.CharField(choices=[('1', 'Aburrido'), ('2', 'No es muy Interesante'), ('3', 'Es algo Entretenido'), ('4', 'Es un Buen Libro'), ('5', 'Excelente Libro')], default=0, max_length=1),
        ),
    ]
