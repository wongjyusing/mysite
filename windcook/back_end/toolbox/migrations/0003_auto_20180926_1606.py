# Generated by Django 2.1.1 on 2018-09-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0002_about_booklink_friendlink_home_spacelink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='home',
            name='slug',
        ),
    ]