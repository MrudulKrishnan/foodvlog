# Generated by Django 2.2 on 2023-03-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20230330_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
