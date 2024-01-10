from django.shortcuts import render

# Create your views here.
# TuneTracker/views.py
from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'TuneTracker/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})
