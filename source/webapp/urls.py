from django.urls import path

from webapp.views import index, create_entry, update_entry

urlpatterns = [
    path('', index, name='entries'),
    path('entries/add', create_entry, name='create_entry'),
    path('entries/<int:pk>/', update_entry, name='update_entry'),
]