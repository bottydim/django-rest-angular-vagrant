from django.contrib import admin

from stream.categories.models import Category

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'description', 'owner')
admin.site.register(Category)
