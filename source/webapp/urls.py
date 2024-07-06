from django.urls import path

from webapp.views import index, create_entry

urlpatterns = [
    path('', index, name='entries'),
    path('entries/add', create_entry, name='create_entry'),
]