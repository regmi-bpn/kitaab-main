# Generated by Django 3.2.4 on 2021-07-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
