from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_published')
    list_display_links = ('title',)
    readonly_fields = ('created_date','last_modified')
    list_filter = ('title', 'created_date', 'published_date')
    search_fields = ('title', 'content')


admin.site.register(Article, ArticleAdmin)