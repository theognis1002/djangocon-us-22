from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Genre(models.Model):
    POP = "pop"
    COUNTRY = "country"
    RNB = "rnb"
    HIP_HOP = "hip_hop"
    GOSPEL = "gospel"
    KPOP = "kpop"
    ROCK = "rock"
    TECHNO = "techno"
    FLAMENCO = "flamenco"
    CLASSICAL = "classical"

    GENRE_CHOICES = [
        (POP, "Pop"),
        (COUNTRY, "Country"),
        (RNB, "Rhythm & Blues"),
        (HIP_HOP, "Hip Hop"),
        (GOSPEL, "Gospel"),
        (KPOP, "K-Pop"),
        (ROCK, "Rock 'N Roll"),
        (TECHNO, "Techno/Dance"),
        (FLAMENCO, "Flamenco"),
        (CLASSICAL, "Classical"),
    ]

    name = models.CharField(max_length=150, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name


class RecordLabel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateTimeField()
    hometown = models.CharField(max_length=150, blank=True, null=True)
    record_label = models.ForeignKey(RecordLabel, on_delete=models.CASCADE, related_name="recording_artists")

    def __str__(self):
        return self.name

    @property
    def age(self):
        return (timezone.now() - self.birth_date).years


class Album(models.Model):
    name = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs", blank=True, null=True)
    time_length = models.TimeField()

    def __str__(self):
        return f"{self.artist} - {self.name}"


class Playlist(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return str(self.pk)
