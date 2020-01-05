from django.contrib import admin
from basic_app.models import Customer, Van, Driver
# Register your models here.

admin.site.register(Customer)
admin.site.register(Van)
# admin.site.register(VanRental)
admin.site.register(Driver)