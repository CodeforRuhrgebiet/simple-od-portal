from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import (DatasetListView,
                    DatasetDetailView,
                    DatasetSearchView,
                    TagListView,
                    TagDetailView)


urlpatterns = [
    url(r'^$', DatasetListView.as_view(), name='dataset-list'),
    url(r'^tags/$', TagListView.as_view(), name='tag-list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag-detail'),
    url(r'^%s/$' % _('search'), DatasetSearchView.as_view(), name='dataset-search'),
    url(r'^(?P<slug>[-\w]+)/$', DatasetDetailView.as_view(), name='dataset-detail'),
]
