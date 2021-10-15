from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import generics
from .serializers import PlaylistSerializer
from .models import Playlist

# Create your views here.
class PlaylistView(generics.CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer



def main(request):
    return render(request, 'frontend/index.html')