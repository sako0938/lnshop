# Generated by Django 3.0.9 on 2020-08-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200805_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sats_per_dollar',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='734bb279e43a4459b5dc075b39487786', max_length=32),
        ),
    ]
