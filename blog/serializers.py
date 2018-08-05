from rest_framework import serializers
from blog.models import BlogEntryFile, BlogEntry


class BlogEntryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntryFile


class BlogEntrySerializer(serializers.ModelSerializer):
    files = BlogEntryFileSerializer(source='files', many=True)

    class Meta:
        model = BlogEntry
        fields = ('id', 'title', 'body', 'link', 'preview',
                  'description', 'likes', 'created_at', 'files')
        read_only_fields = ('id', 'preview', 'description',
                            'likes', 'created_at')
