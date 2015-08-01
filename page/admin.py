from django.contrib import admin

from .models import Tag, Page, Category

# Register your models here.

admin.site.register(Tag)
admin.site.register(Page)
admin.site.register(Category)
