# Generated by Django 2.2.6 on 2019-10-31 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='Catagory',
            field=models.CharField(max_length=50, verbose_name='Catagory'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='CreateDate',
            field=models.DateField(default=datetime.date.today, editable=False, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='Description',
            field=models.CharField(max_length=50, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='Name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='PriceDescription',
            field=models.CharField(max_length=50, verbose_name='Price'),
        ),
    ]
