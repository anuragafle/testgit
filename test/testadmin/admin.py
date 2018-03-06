from django.contrib import admin
from .models import User
class UserClass(admin.ModelAdmin):
    list_display = ('username','email','password','activated')
admin.site.register(User,UserClass)