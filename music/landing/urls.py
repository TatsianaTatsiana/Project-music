from django.urls import path, re_path
from landing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.ArtistView.as_view(), name='artist'),
    re_path('song/addlikes/(?P<song_id>[0-9]+)/$', views.addlike, name='song'),
    path('contact/', views.contact, name="contact"),
    path('mission/', views.mission, name="mission")
]