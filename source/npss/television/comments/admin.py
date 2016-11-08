from django.contrib import admin

from television.comments.models import Comment

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'owner')

admin.site.register(Comment)
