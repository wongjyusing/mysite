# Generated by Django 2.1 on 2018-09-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180915_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_tag',
            field=models.ManyToManyField(related_query_name='card', to='blog.BlogTag', verbose_name='博客标签'),
        ),
    ]
