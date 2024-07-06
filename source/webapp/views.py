from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Entry
from webapp.forms import EntryForm, SearchForm


def index(request):
    entry_form = EntryForm()

    if request.method == 'POST':
        return create_entry(request)

    if request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            search = search_form.cleaned_data['query']
            entries = Entry.objects.filter(name=search)
            return render(request, 'index.html', context={'entries': entries, 'search_form': search_form, 'entry_form': entry_form})

        entries = Entry.objects.filter(status='active').order_by('created_at')
        return render(request, 'index.html', context={'entries': entries, 'search_form': search_form, 'entry_form': entry_form})

    search_form = SearchForm()
    entries = Entry.objects.filter(status='active').order_by('created_at')
    return render(request, 'index.html', context={'entries': entries, 'search_form': search_form, 'entry_form': entry_form})


def create_entry(request):
    form = EntryForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('entries')
    else:
        return render(request, 'create_entry.html', {'form': form})

