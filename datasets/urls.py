from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import DatasetListView, DatasetDetailView


urlpatterns = [
    url(r'^$', DatasetListView.as_view(), name='dataset-list'),
    url(r'^(?P<slug>[-\w]+)/$', DatasetDetailView.as_view(), name='dataset-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
