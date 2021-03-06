"""simple_od_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _

from datasets.sitemaps import DatasetSitemap, TagsSitemap
from datasets.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^%s/' % _('datasets'), include('datasets.urls')),
    url(r'^$', index),
    url(r'^sitemap\.xml$', sitemap, {
        'sitemaps': {
            'flatpages': FlatPageSitemap,
            'datasets': DatasetSitemap,
            'tags': TagsSitemap
        }
    }, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    urlpatterns += static(settings.DATASETS_URL, document_root=settings.DATASETS_ROOT)
