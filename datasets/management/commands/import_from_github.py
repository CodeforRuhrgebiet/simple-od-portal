from django.conf import settings
from django.core.management.base import BaseCommand

from ...loader import get_datasets
from ...models import Dataset


class Command(BaseCommand):
    help = 'Load datasets from github repo folder into database.'

    def handle(self, *args, **options):
        datasets = get_datasets()
        for data in datasets:
            Dataset.create_from_yaml(data, overwrite=True)
        self.stdout.write(self.style.SUCCESS(
            'Successfully imported %s datasets from %s' % (
                len(datasets),
                settings.DATASETS_ROOT
            )
        ))
