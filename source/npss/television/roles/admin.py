from django.contrib import admin

from television.roles.models import Role

# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')

admin.site.register(Role)
