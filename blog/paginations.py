from rest_framework.pagination import PageNumberPagination


class BlogEntryPagination(PageNumberPagination):
    page_size = 100
