# Generated by Django 2.1.2 on 2018-11-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181030_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(default='/templates/no_image_available.png', upload_to=''),
        ),
    ]
