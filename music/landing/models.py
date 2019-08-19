from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='image', blank=True)


    def __str__(self):
        return self.name

'''    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url'''


class Song(models.Model):
    CHOICE_LANG = (('rus', 'Russian'),
                   ('eng', 'English'),)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')#появится поле songs в классе Artist
    title = models.CharField(max_length=60)
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    language = models.CharField(max_length=50, choices=CHOICE_LANG)
    song_likes = models.IntegerField(default='0')
    artist_song = models.FileField(upload_to='mp3', blank=True)

    def __str__(self):
        return self.title
