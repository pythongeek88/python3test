# Generated by Django 2.1.2 on 2018-10-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]