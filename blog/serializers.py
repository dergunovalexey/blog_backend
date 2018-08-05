from rest_framework import serializers
from blog.models import BlogEntryFile, BlogEntry


class BlogEntryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntryFile
        fields = ('file', )


class BlogEntrySerializer(serializers.ModelSerializer):
    files = BlogEntryFileSerializer(many=True, required=False)
    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M',
                                           read_only=True)

    class Meta:
        model = BlogEntry
        fields = ('id', 'author', 'title', 'body', 'link', 'preview',
                  'description', 'likes', 'created_at', 'files')
        read_only_fields = ('id', 'author', 'preview', 'description',
                            'likes', 'created_at')

    def create(self, validated_data):
        files = validated_data.pop('files', [])
        instance = super().create(validated_data)
        obj_list = []
        for f in files:
            obj_list.append(BlogEntryFile(
                blog_entry_id=instance['id'],
                file=f
            ))

        if obj_list:
            BlogEntryFile.objects.bulk_create(obj_list, 100)
        return instance


class BlogEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ('id', 'author', 'title', 'likes', 'created_at')
        read_only_fields = ('id', 'author', 'likes', 'created_at')
