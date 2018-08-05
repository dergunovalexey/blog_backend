from django.conf.urls import url, include

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
]
