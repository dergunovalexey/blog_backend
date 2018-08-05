from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, DestroyModelMixin)

from blog.models import BlogEntry
from blog.paginations import BlogEntryPagination
from blog.serializers import BlogEntrySerializer


class BlogEntryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                       DestroyModelMixin, GenericViewSet):
    queryset = BlogEntry.objects.all().order_by('-created_at')
    pagination_class = BlogEntryPagination
    serializer_class = BlogEntrySerializer

    def perform_create(self, serializer):
        serializer.save(author=serializer.context['request'].user)
