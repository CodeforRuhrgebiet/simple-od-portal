from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import uuid

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from .utils import slugify


@python_2_unicode_compatible
class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    csv_file = models.FileField(upload_to='data', max_length=500)
    tags_raw = models.CharField(max_length=256, blank=True, null=True,
                                help_text=_('Enter comma seperated tags'))
    description = models.TextField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dataset-detail', kwargs={'slug': self.slug})

    @cached_property
    def tags(self):
        if self.tags_raw:
            return self.tags_raw.split(',')
        return []
