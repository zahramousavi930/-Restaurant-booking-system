# Generated by Django 4.2.7 on 2023-11-24 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_module', '0004_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_menu',
            name='like',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
