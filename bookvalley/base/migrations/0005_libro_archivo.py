# Generated by Django 4.2 on 2023-05-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_libro_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='archivo',
            field=models.FileField(null=True, upload_to='archivos'),
        ),
    ]
