from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AlbumItems(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField()
    ordering_priority = models.IntegerField()

    def __str__(self):
        return f'{self.album} - {self.image}'

    class Meta:
        verbose_name_plural = "Album Items"
