from django.db import models
from django.contrib.postgres.fields import ArrayField


class BlogEntry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=128)
    body = models.TextField()
    link = models.URLField(blank=True, null=True)
    preview = models.ImageField(upload_to='blog/blog_entry/preview/',
                                blank=True, null=True)
    description = models.TextField(blank=True)
    likes = ArrayField(models.IntegerField(), default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogEntryFile(models.Model):
    blog_entry = models.ForeignKey('blog.BlogEntry')
    file = models.FileField(upload_to='blog/blog_entry/file/')

    def __str__(self):
        return 'File to '.format(self.blog_entry.title)
