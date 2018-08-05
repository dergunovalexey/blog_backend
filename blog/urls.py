from rest_framework.routers import DefaultRouter
from blog.views import BlogEntryViewSet


router = DefaultRouter()
router.register(r'blog_entry', BlogEntryViewSet, 'blog_entry')

urlpatterns = router.urls
