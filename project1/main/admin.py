from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
# class useradmin(admin.ModelAdmin):
#     list_display =('id','name','email','password')

# admin.site.register(user, useradmin)
# admin.site.register(formdata)