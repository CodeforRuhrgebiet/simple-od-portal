from django.contrib.sitemaps import Sitemap

from .models import Dataset


class DatasetSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Dataset.objects.all()

    def lastmod(self, obj):
        return obj.created_ts
