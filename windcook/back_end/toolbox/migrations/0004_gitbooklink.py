# Generated by Django 2.1.1 on 2018-09-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0003_auto_20180926_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitBookLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='链接名称')),
                ('link', models.URLField(help_text='请填写http或https开头的完整形式地址', verbose_name='书籍链接')),
                ('book_status', models.CharField(default='未完成', max_length=50, verbose_name='状态')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍链接列表',
                'ordering': ['id'],
            },
        ),
    ]
