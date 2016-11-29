from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from . models import Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        exclude = ('last_modified', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_published')
    list_display_links = ('title',)
    readonly_fields = ('created_date','last_modified')
    list_filter = ('title', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    form = ArticleAdminForm



admin.site.register(Article, ArticleAdmin)

