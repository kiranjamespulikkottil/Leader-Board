# Generated by Django 2.0.3 on 2018-03-29 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_auto_20180326_0708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-score']},
        ),
    ]
