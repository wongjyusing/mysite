# Generated by Django 2.1.1 on 2018-09-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('body', models.TextField(verbose_name='文章')),
                ('author', models.CharField(default='sing', max_length=50, verbose_name='作者')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('slug', models.SlugField(unique=True, verbose_name='后缀')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(verbose_name='简介')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签列表',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tag',
            field=models.ManyToManyField(related_name='blog_card', to='blog.BlogTag', verbose_name='博客标签'),
        ),
    ]
