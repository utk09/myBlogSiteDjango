# Generated by Django 2.1.7 on 2019-03-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190324_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]