from django.urls import path
from .views import HomeView, EntryDetail, CreateEntry


urlpatterns = [
    path('index', HomeView.as_view(), name='index'),
    path('detail/<int:pk>/', EntryDetail.as_view(), name='detail'),
    path('create', CreateEntry.as_view(success_url = 'index'), name='create'),
]
