from django.contrib import admin

# Register your models here.
from .models import Material,Scale,Supplier

admin.site.register(Material)
admin.site.register(Scale)
admin.site.register(Supplier)