# Generated by Django 3.0.9 on 2020-08-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200804_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price_ht',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='d815508484494223bd45551a904ccae6', max_length=32),
        ),
    ]
