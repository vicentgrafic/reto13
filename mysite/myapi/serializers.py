from rest_framework import serializers
from .models import game, room, roomUser, roomChat, userChat
import django.contrib.auth.models   #modelo de usuarios de django

class loginSerializer(serializers.ModelSerializer):

    class Meta:
        # modelo de datos de django
        model = django.contrib.auth.models.User
        #fields = ('username', 'email', )

class userSerializer(serializers.ModelSerializer):

    class Meta:
        # modelo de datos de django
        model = django.contrib.auth.models.User
        fields = ('username', 'email', )

class userChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userChat
        fields = ('message', 'user','user_destination')


class gameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = game
        fields = ('name', 'created_date', )

class roomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = room
        fields = ('name', 'maximum_players', 'created_by', 'game')

class roomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = roomUser
        fields = ('room', 'user', )

'''class chatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = chat
        fields = ('message', 'room', 'user', )'''

class roomChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = roomChat
        fields = ('message', 'room', 'user',)