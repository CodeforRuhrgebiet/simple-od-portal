from django.contrib.sitemaps import Sitemap

from .models import Dataset, Tag


class DatasetSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Dataset.objects.all()

    def lastmod(self, obj):
        return obj.created_ts


class TagsSitemap(DatasetSitemap):
    def items(self):
        return Tag.objects.all()
