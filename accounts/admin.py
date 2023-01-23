from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userId', 'firstName', 'password']
    list_display_links = ['id', 'userId', 'firstName']
