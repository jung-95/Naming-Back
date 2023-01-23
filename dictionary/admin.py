from django.contrib import admin
from dictionary.models import *

@admin.register(dictionary)
class dictionaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border']
    list_display_links = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border']

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'consonant', 'contents']
    list_display_links = ['id', 'consonant', 'contents']