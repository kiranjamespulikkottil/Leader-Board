# Generated by Django 2.0.3 on 2018-03-29 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_auto_20180329_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='scoreadmin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
