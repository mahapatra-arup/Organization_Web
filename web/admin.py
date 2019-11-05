from django.contrib import admin

# Register your models here.
from .models import ProductDetails,Org_History


#model Configration
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price','Description')
    list_filter = ('Name', 'Price','Description')

class Org_HistoryAdmin(admin.ModelAdmin):
    list_display = ('Tittle', 'Sub_Tittle','Description')
    list_filter = ('Tittle', 'Sub_Tittle','Description')


# Register your models here.
admin.site.register(ProductDetails,ProductDetailsAdmin)
admin.site.register(Org_History,Org_HistoryAdmin)

