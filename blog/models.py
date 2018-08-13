from django.db import models
from django.contrib.postgres.fields import ArrayField
from blog.tasks import get_preview_description


class BlogEntry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=128)
    body = models.TextField()
    link = models.URLField(blank=True)
    preview = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    likes = ArrayField(models.IntegerField(), default=list, blank=True,
                       help_text='users id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            id = False
        else:
            id = True
        # delete duplicate elements
        self.likes = list(set(self.likes))

        super().save(*args, **kwargs)

        if not id:
            # get description and preview from link
            get_preview_description.apply_async(args=(self.id, ))


class BlogEntryFile(models.Model):
    blog_entry = models.ForeignKey('blog.BlogEntry', related_name='files')
    file = models.FileField(upload_to='blog/blog_entry/file/')

    def __str__(self):
        return 'File to '.format(self.blog_entry.title)
