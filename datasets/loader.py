import os
import yaml

from django.conf import settings


datasets_fp = os.path.join(settings.DATASETS_ROOT, settings.DATASETS_INDEX)


def get_datasets():
    return yaml.load(open(datasets_fp, encoding='utf8'))
