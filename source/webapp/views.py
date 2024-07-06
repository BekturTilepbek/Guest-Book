from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Entry
from webapp.forms import EntryForm, SearchForm, DeleteEntryForm


def index(request):
    entry_form = EntryForm()

    if request.method == 'POST':
        return create_entry(request)

    if request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            search = search_form.cleaned_data['query']
            entries = Entry.objects.filter(name=search).order_by('-created_at')
            return render(request, 'index.html', context={
                'entries': entries,
                'search_form': search_form,
                'entry_form': entry_form})

        entries = Entry.objects.filter(status='active').order_by('-created_at')
        return render(request, 'index.html', context={
            'entries': entries,
            'search_form': search_form,
            'entry_form': entry_form})

    search_form = SearchForm()
    entries = Entry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={
        'entries': entries,
        'search_form': search_form,
        'entry_form': entry_form})


def create_entry(request):
    if request.method == 'GET':
        entry_form = EntryForm()
        return render(request, 'create_entry.html', context={'entry_form': entry_form})
    else:
        entry_form = EntryForm(data=request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('entries')
        else:
            return render(request, 'create_entry.html', {'entry_form': entry_form})


def update_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        entry_form = EntryForm(instance=entry)
        return render(request, 'update_entry.html', {'entry_form': entry_form})
    else:
        entry_form = EntryForm(request.POST, instance=entry)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('entries')
        else:
            return render(request, 'update_entry.html', {'entry_form': entry_form})


def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        delete_form = DeleteEntryForm()
        return render(request, 'delete_entry.html', {'entry': entry, 'delete_form': delete_form})
    else:
        delete_form = DeleteEntryForm(data=request.POST, author_email=entry.email)
        if delete_form.is_valid():
            entry.delete()
            return redirect('entries')
        else:
            return render(request, 'delete_entry.html', {'entry': entry, 'delete_form': delete_form})
