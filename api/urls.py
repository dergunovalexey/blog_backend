from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^doc/', schema_view),
]
