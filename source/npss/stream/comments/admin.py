from django.contrib import admin

from stream.comments.models import Comment

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'owner')

admin.site.register(Comment)
