from django.urls import path
from .views import PlaylistView

urlpatterns = [
    path('playlist', PlaylistView.as_view())
]
