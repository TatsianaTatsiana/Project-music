from django import views

from .models import Artist
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from landing.models import Song
from django.http import HttpResponseRedirect


def index(request):
    song_list = Song.objects.all()
    context_dict = {'song': song_list}
    return render(request, 'landing/list_songs.html', context_dict)


class ArtistView(views.View):
    template_name = 'landing/artist.html'

    def get(self, request, artist_id):
        return render(request, self.template_name, {'artists': Artist.objects.all().order_by('name')})




def addlike(request, song_id):
   song = get_object_or_404(Song, id=song_id)  # возвращает id песни или 404.
   song.song_likes += 1 # Прибавляет единицу к song_likes
   song.save() # сохраняет
   return HttpResponseRedirect('/') # делает редирект на ту же страницу


def contact(request):
    return render(request, 'landing/contact.html',
                  {'values': ['+ 375 (29) 068-68-68', 'example@mail.ru', 'skype', 'facebook', 'vk']})


def mission(request):
    return render(request, 'landing/mission.html')

