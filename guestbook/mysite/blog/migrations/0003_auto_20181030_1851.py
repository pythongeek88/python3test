# Generated by Django 2.1.2 on 2018-10-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug'),
        ),
    ]
