from django.contrib import admin

from television.users.models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username',
#                     'email',
#                     'password',
#                     'first_name',
#                     'last_name',
#                     'data_joined',
#                     'last_login',
#                     'last_login_ip',
#                     'role')

admin.site.register(User)
