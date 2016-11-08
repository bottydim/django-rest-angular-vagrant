from django.contrib import admin

from television.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'category', 'text')
