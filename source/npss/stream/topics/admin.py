from django.contrib import admin

from stream.topics.models import Topic

# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('id',
#                     'title',
#                     'description',
#                     'views_count',
#                     'created_on',
#                     'owner',
#                     'deleted_on',
#                     'comment')
admin.site.register(Topic)
