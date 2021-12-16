from django.contrib import admin
from .models import game, room, roomUser, roomChat, userChat

# Register your models here.
admin.site.register(game)
admin.site.register(room)
admin.site.register(roomChat)
admin.site.register(roomUser)
admin.site.register(userChat)