# Generated by Django 4.2.7 on 2023-11-26 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_module', '0011_remove_reservation_user_reservation_w_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='w_user',
            new_name='add_user',
        ),
    ]