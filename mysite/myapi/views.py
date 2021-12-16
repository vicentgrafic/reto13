from rest_framework import viewsets
from .models import game, room, roomUser, roomChat, userChat
from .serializers import userSerializer, gameSerializer, roomSerializer, roomUserSerializer, roomChatSerializer, userChatSerializer
from django.contrib.auth.models import User # modelo de datos de usuarios

# Create your views here.

class userViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

class gameViewSet(viewsets.ModelViewSet):
    queryset = game.objects.all().order_by('name')
    serializer_class = gameSerializer

class roomViewSet(viewsets.ModelViewSet):
    queryset = room.objects.all().order_by('name')
    serializer_class = roomSerializer

class roomUserViewSet(viewsets.ModelViewSet):
    queryset = roomUser.objects.all().order_by('id')
    serializer_class = roomUserSerializer

    # Filtros para búsquedas mediante REST
    filter_fields = (
        'user',
    )

class roomChatViewSet(viewsets.ModelViewSet):
    queryset = roomChat.objects.all().order_by('id')
    serializer_class = roomChatSerializer

    # Filtros para búsquedas mediante REST
    filter_fields = (
        'user',
        'room',
    )

class userChatViewSet(viewsets.ModelViewSet):
    queryset = userChat.objects.all().order_by('id')
    serializer_class = userChatSerializer

    # Filtros para búsquedas mediante REST
    filter_fields = (
        'user',
        'user_destination',
    )

################### Función que recoje la petición GET (con decorador) de la vista "welcome" ##########################
from django.http import JsonResponse
from django.http import HttpResponseForbidden
def welcome(request):

    print("welcome > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)

    if request.user.is_authenticated == False:
        print("welcome > is_authenticated = False > Error")
        return HttpResponseForbidden()

    if request.method == 'GET':
        content = {"message": "Welcome To Steam " + str(request.user) + "!"}  # diccionario con formato JSON

    elif request.method == 'POST':
        content = {"message": "welcome Error..."}

    return JsonResponse(content)
#######################################################################################################################

##########################  EVENTO DE LOGIN ###########################################################################
from django.contrib.auth.signals import user_logged_in
def user_log(sender, user, request, **kwargs):

    print("django.contrib.auth.signals.user_logged_in")

user_logged_in.connect(user_log)
#######################################################################################################################