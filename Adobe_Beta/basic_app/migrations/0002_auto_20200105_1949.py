# Generated by Django 2.2.5 on 2020-01-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='van',
            name='tag_exp',
        ),
    ]
