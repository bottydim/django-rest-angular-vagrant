from django.contrib import admin

from television.videos.models import Video

# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('id',
#                     'title',
#                     'description',
#                     'views_count',
#                     'created_on',
#                     'owner',
#                     'deleted_on',
#                     'comment',
#                     'category')

admin.site.register(Video)
