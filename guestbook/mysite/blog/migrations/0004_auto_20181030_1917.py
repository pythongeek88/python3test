# Generated by Django 2.1.2 on 2018-10-30 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181030_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-posted']},
        ),
    ]
