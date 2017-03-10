from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import os
import uuid

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from .utils import slugify


@python_2_unicode_compatible
class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_ts = models.DateTimeField(_('Created at'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=500, unique=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, editable=False)
    file_path = models.FilePathField(verbose_name=_('File path'),
                                     path=settings.DATASETS_ROOT,
                                     recursive=True)
    file_path_relative = models.CharField(max_length=500, editable=False)
    source_name = models.CharField(_('Source name'), max_length=500)
    source_url = models.URLField(_('Source url'), blank=True, null=True)
    published_date = models.DateField(_('Published date'), blank=True, null=True)
    file_content = models.TextField(_('File content'), editable=False)
    tags_raw = models.CharField(_('Tags'), max_length=256, blank=True, null=True,
                                help_text=_('Enter comma seperated tags'))
    description = models.TextField(_('Description'), blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.file_content = self.get_file_content()
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

    @cached_property
    def download_url(self):
        return settings.DATASETS_URL + self.file_path_relative

    @cached_property
    def preview(self):
        return self.get_preview()

    def get_file_content(self):
        try:
            with open(self.file_path, encoding='utf-8') as f:
                content = f.read()
            return content
        except (UnicodeDecodeError, UnicodeEncodeError) as e:
            return str(e)

    def get_preview(self):
        try:
            with open(self.file_path, encoding='utf-8') as f:
                lines = f.readlines()[:6]
            return {
                'header': lines[0].split(','),
                'subset': [l.split(',') for l in lines[1:]]
            }
        except (UnicodeDecodeError, UnicodeEncodeError):
            return False

    @classmethod
    def create_from_yaml(cls, data, overwrite=False):
        slug = slugify(data['name'])
        if overwrite:
            cls.objects.filter(slug=slug).delete()
        if not cls.objects.filter(slug=slug).exists():
            dataset = cls(
                name=data['name'],
                file_path=os.path.join(settings.DATASETS_ROOT, data['file']),
                file_path_relative=data['file'],
                source_name=data['source'],
                tags_raw=', '.join(data.get('tags', [])),
                description=data.get('description', None),
                source_url=data.get('url', None),
                published_date=data.get('pub_date', None)
            )
            dataset.save()
