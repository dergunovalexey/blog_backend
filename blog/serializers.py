from rest_framework import serializers
from blog.models import BlogEntryFile, BlogEntry


class BlogEntryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntryFile
        fields = ('file', )


class BlogEntrySerializer(serializers.ModelSerializer):
    files = BlogEntryFileSerializer(many=True, required=True)

    class Meta:
        model = BlogEntry
        fields = ('id', 'author', 'title', 'body', 'link', 'preview',
                  'description', 'likes', 'created_at', 'files')
        read_only_fields = ('id', 'author', 'preview', 'description',
                            'likes', 'created_at')


class BlogEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ('id', 'author', 'title', 'likes', 'created_at')
        read_only_fields = ('id', 'author', 'likes', 'created_at')
