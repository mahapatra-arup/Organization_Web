from django.db import models
import datetime
import uuid
from django.contrib import admin

#Admin Header
admin.site.site_header="DTL"
admin.site.site_title="Product Detail"



'''__all__ = [
    'AutoField', 'BLANK_CHOICE_DASH', 'BigAutoField', 'BigIntegerField',
    'BinaryField', 'BooleanField', 'CharField', 'CommaSeparatedIntegerField',
    'DateField', 'DateTimeField', 'DecimalField', 'DurationField',
    'EmailField', 'Empty', 'Field', 'FieldDoesNotExist', 'FilePathField',
    'FloatField', 'GenericIPAddressField', 'IPAddressField', 'IntegerField',
    'NOT_PROVIDED', 'NullBooleanField', 'PositiveIntegerField',
    'PositiveSmallIntegerField', 'SlugField', 'SmallIntegerField', 'TextField',
    'TimeField', 'URLField', 'UUIDField',
]'''

# Create your models here.
class ProductDetails(models.Model):
    ProductId =models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    Name=models.CharField(verbose_name="Name",max_length=50)
    Catagory=models.CharField(verbose_name="Catagory",max_length=50)
    Description=models.CharField(verbose_name="Description",max_length=50)
    Price=models.DecimalField(verbose_name="Price",max_digits=10,decimal_places=2)
    PriceDescription=models.CharField(verbose_name="Price Description",max_length=50)
    CreateDate =  models.DateField(verbose_name="Date", default=datetime.date.today,editable=False)

    def __str__(self):
       return self.Name