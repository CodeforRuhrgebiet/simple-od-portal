from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import DatasetListView, DatasetDetailView, DatasetSearchView


urlpatterns = [
    url(r'^$', DatasetListView.as_view(), name='dataset-list'),
    url(r'^%s/$' % _('search'), DatasetSearchView.as_view(), name='dataset-search'),
    url(r'^(?P<slug>[-\w]+)/$', DatasetDetailView.as_view(), name='dataset-detail'),
]
