from django.contrib import admin

# Register your models here.
from .models import Material,Scale,Supplier,MaterialTransaction,quotation, quotationAmount, quotationitem, quotationNumber, quotationsize

admin.site.register(Material)
admin.site.register(Scale)
admin.site.register(Supplier)
admin.site.register(MaterialTransaction)

admin.site.register(quotation)
admin.site.register(quotationAmount)
# admin.site.register(quotationclient)
admin.site.register(quotationitem)
admin.site.register(quotationNumber)
admin.site.register(quotationsize)
