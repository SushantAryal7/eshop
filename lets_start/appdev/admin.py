from django.contrib import admin
from .models import Brand, Index, Customer, Order


# Register your models here.


admin.site.register(Brand)
admin.site.register(Index)
admin.site.register(Customer)
admin.site.register(Order)

