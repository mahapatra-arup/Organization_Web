# Generated by Django 2.2.6 on 2019-10-31 17:15

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('ProductId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Name', models.TextField(max_length=50, verbose_name='Name')),
                ('Catagory', models.TextField(max_length=50, verbose_name='Catagory')),
                ('Description', models.TextField(max_length=50, verbose_name='Description')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('PriceDescription', models.TextField(max_length=50, verbose_name='Price')),
                ('CreateDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
