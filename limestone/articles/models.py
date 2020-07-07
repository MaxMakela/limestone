from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_article')
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)], unique=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at', 'updated_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    content = models.TextField(max_length=500)
    add_at = models.DateTimeField(default=timezone.now)

    @property
    def is_article_author(self):
        return self.article.author is self.author

    def __str__(self):
        return self.content


class Tag(models.Model):
    title = models.CharField(max_length=35)
    slug = models.TextField(max_length=250)
    article = models.ManyToManyField(Article, related_name='tag')

    # class Meta:
    #     ordering = ['get_rating']

    @property
    def rating(self):
        return len(self.article.all())

    def __str__(self):
        return self.title

