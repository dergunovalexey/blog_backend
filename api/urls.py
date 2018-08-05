from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^doc/', schema_view),
    url(r'^token-auth/', views.obtain_auth_token)
]
