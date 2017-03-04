from django.views.generic import ListView, DetailView

from .models import Dataset


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(DetailView):
    model = Dataset
