from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    short_content = RichTextField(blank=True)
    image = models.ImageField(upload_to='articles_uploads/')
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.title



