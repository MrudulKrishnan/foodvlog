# Generated by Django 2.2 on 2023-03-31 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20230331_1119'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.CartList')),
                ('item_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Dishes')),
            ],
        ),
    ]