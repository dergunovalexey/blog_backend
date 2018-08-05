from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, DestroyModelMixin)

from blog.models import BlogEntry


class BlogEntryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                       DestroyModelMixin, GenericViewSet):
    queryset = BlogEntry.objects.all().order_by('-created_at')