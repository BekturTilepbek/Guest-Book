from django.urls import path

from webapp.views import index, create_entry, update_entry, delete_entry

urlpatterns = [
    path('', index, name='entries'),
    path('entries/add', create_entry, name='create_entry'),
    path('entries/<int:pk>/update', update_entry, name='update_entry'),
    path('entries/<int:pk>/delete', delete_entry, name='delete_entry'),
]
