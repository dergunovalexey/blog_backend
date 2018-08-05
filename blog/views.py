from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, DestroyModelMixin)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import BlogEntry
from blog.paginations import BlogEntryPagination
from blog.serializers import BlogEntryListSerializer, BlogEntrySerializer
from blog.permissions import BlogEntryPermission


class BlogEntryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                       DestroyModelMixin, GenericViewSet):
    queryset = BlogEntry.objects.all().order_by('-created_at')
    pagination_class = BlogEntryPagination
    serializer_class = BlogEntryListSerializer
    permission_classes = (BlogEntryPermission, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=serializer.context['request'].user)

    def get_serializer_class(self):
        if self.action in ('retrieve', 'create'):
            return BlogEntrySerializer

        return super().get_serializer_class()

    @action(methods=['get'],permission_classes=(IsAuthenticated, ), detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        user_id = request.user.id
        if user_id in obj.likes:
            obj.likes.remove(user_id)
        else:
            obj.likes.append(user_id)
        obj.save()
        return Response()
