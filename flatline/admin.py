from django.contrib import admin

# Register your models here.

from .models import User, UserBill, Bill, Flat

admin.site.register(User)
admin.site.register(UserBill)
admin.site.register(Flat)
admin.site.register(Bill)
