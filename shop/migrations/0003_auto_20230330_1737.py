# Generated by Django 2.2 on 2023-03-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_dishes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
