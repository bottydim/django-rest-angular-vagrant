from django.contrib import admin

from television.pictures.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'description',
                    'views_count',
                    'created_on',
                    'owner',
                    'deleted_on',
                    'comment')
