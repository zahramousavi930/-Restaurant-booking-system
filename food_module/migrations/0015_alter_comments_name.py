# Generated by Django 4.2.7 on 2023-12-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_module', '0014_alter_food_menu_like_user_alter_food_menu_user_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]