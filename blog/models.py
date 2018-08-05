from django.db import models


class BlogEntry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=128)
    body = models.TextField()
    link = models.URLField(blank=True, null=True)
    preview = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
