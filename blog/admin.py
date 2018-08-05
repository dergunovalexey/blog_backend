from django.contrib import admin
from blog.models import BlogEntry, BlogEntryFile


class BlogEntryFileInline(admin.TabularInline):
    model = BlogEntryFile


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('id', 'author__username', 'title', 'body')
    ordering = ('-created_at', )
    inlines = (BlogEntryFileInline, )
