# Generated by Django 4.2.4 on 2023-08-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplannerapp', '0004_alter_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=250),
        ),
    ]
