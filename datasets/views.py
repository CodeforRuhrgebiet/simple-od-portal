from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

from .models import Dataset


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(DetailView):
    model = Dataset


def index(request, *args, **kwargs):
    return redirect('dataset-list')
