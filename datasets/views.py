from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

from .models import Dataset


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(DetailView):
    model = Dataset


class DatasetSearchView(ListView):
    model = Dataset
    template_name = 'datasets/dataset_search.html'

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q and len(q) > 3:
            qs = super().get_queryset().filter(
                Q(name__icontains=q) |
                Q(tags_raw__icontains=q) |
                Q(description__icontains=q) |
                Q(file_content__icontains=q)
            ).order_by('name').distinct()
            if qs:
                return qs
        return []


def index(request, *args, **kwargs):
    return redirect('dataset-list')
