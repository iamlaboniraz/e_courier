from django.contrib import admin
from .models import delivery_product,types_of_product,driver

admin.site.register(delivery_product)
admin.site.register(types_of_product)
admin.site.register(driver)