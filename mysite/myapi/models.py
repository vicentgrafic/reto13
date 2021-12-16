from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    maximum_players = models.PositiveIntegerField(default=20)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey(game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class roomUser(models.Model):
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    #def __str__(self):
    #    return self.room

class roomChat(models.Model):
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message

# user_destination tiene un nombre marcado especialmente ya que hago uso del mismo campo relacionado dos veces
class userChat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_destination = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_destination')
    message = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
