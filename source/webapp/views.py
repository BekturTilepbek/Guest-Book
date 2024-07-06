from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Entry
from webapp.forms import EntryForm, SearchForm


def index(request):
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['query']
            entries = Entry.objects.filter(name=search)
            return render(request, 'index.html', {'entries': entries, 'form': form})

        entries = Entry.objects.filter(status='active').order_by('created_at')
        return render(request, 'index.html', {'entries': entries, 'form': form})

    form = SearchForm()
    entries = Entry.objects.filter(status='active').order_by('created_at')
    return render(request, 'index.html', context={'entries': entries, 'form': form})
