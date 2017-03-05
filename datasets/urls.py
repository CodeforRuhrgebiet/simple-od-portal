from django.conf.urls import url

from .views import DatasetListView, DatasetDetailView


urlpatterns = [
    url(r'^$', DatasetListView.as_view(), name='dataset-list'),
    url(r'^(?P<slug>[-\w]+)/$', DatasetDetailView.as_view(), name='dataset-detail'),
]
