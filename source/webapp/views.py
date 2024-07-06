from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Entry


def index(request):
    entries = Entry.objects.filter(status='active').order_by('created_at')
    return render(request, 'index.html', context={'entries': entries})
