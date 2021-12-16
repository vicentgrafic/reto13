from .models import room, roomUser, roomChat, userChat, game
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User # modelo de datos de usuarios
from django.db import IntegrityError
import json

@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_create(request):

    print("room_create > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_create Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    name = json.loads(request.body)['name']
    maximum_players = json.loads(request.body)['maximum_players']
    game_name = json.loads(request.body)['game']
    game_instance = game.objects.get(name=game_name)

    content = {"message": "room_create a " + name} # diccionario con formato JSON
    print("room_create > name=", name, "maximum_players=", maximum_players , "game_name=",game_name)

    try:
        # crea un registro
        room.objects.create(name=name, maximum_players=maximum_players, created_by=request.user, game=game_instance)
    except IntegrityError as e:
        print(e.args)
        return HttpResponseForbidden()

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_delete(request):

    print("room_delete > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_delete Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['name']
    try:
         room_instance = room.objects.get(name=room_name)
    except room.DoesNotExist:
        return HttpResponseForbidden()

    print("room_delete > room_instance.created_by = ", room_instance.created_by )

    if room_instance.created_by != request.user:
        return HttpResponseForbidden()

    content = {"message": "room_delete a " + room_name} # diccionario con formato JSON
    print("room_delete > room_name=", room_name, "room_instance.id=", room_instance.id)

    #borra el registro
    room_instance.delete()

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_in(request):

    print("room_in > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_in Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['room']
    room_instance = room.objects.get(name=room_name)

    content = {"message": "room_in a " + str(room_name)} # diccionario con formato JSON
    print("room_in > room_name=", room_name, "room_instance.id=", room_instance.id)

    #crea un registro si no existe ya ese registro (where/if not exists)
    roomUser.objects.update_or_create(user=request.user, room=room_instance)

    #crea un registro
    #roomUser.objects.create(user=request.user, room=room_instance)

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_out(request):

    print("room_out > is_authenticated = ", request.user.is_authenticated, " request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_in room_out..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['room']
    room_instance = room.objects.get(name=room_name)

    content = {"message": "room_out a " + str(room_name)} # diccionario con formato JSON
    print("room_out > room_name=", room_name, "room_instance.id=", room_instance.id)

    # elimina todos los registros filtrando por id_usuario e id_sala
    roomUser.objects.filter(user=request.user.id, room=room_instance).delete()

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def userChat_create(request):

    print("userChat_create > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "userChat_create Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    message = json.loads(request.body)['message']
    user_destination_name = json.loads(request.body)['user_destination']
    user_destination_instance = User.objects.get(username=user_destination_name)

    content = {"message": "userChat_create user_destination=" + user_destination_instance.username + ", message=" + message} # diccionario con formato JSON
    print("userChat_create > user_destination=" + user_destination_instance.username + ", message=" + message)

    # crea un registro
    userChat.objects.create(user=request.user, user_destination=user_destination_instance, message=message)

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def roomChat_create(request):

    print("roomChat_create > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "roomChat_create Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['room']
    message = json.loads(request.body)['message']
    room_instance = room.objects.get(name=room_name)

    content = {"message": "roomChat_create room=" + room_name + ", message=" + message} # diccionario con formato JSON
    print("roomChat_create > room=" + room_name + ", message=" + message)

    # crea un registro
    roomChat.objects.create(room=room_instance, user=request.user, message=message)

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_list_users(request):

    print("room_list_users > is_authenticated = ", request.user.is_authenticated, " request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_list_users"}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['room']
    room_instance = room.objects.get(name=room_name)
    print("room_list_users > room_name=", room_name, "room_instance.id=", room_instance.id)

    # obtiene todas las salas y usuarios sin filtrar
    #values = roomUser.objects.all().select_related('user', 'room').values('room__name','user__username')

    # obtiene los usuarios de las sala especificada
    values = roomUser.objects.filter(room=room_instance.id).select_related('user', 'room').values('user__username')

    for value in values:
        print(value)

    # Convert the QuerySet to a List
    list_of_dicts = list(values)

    # Convert List of Dicts to JSON
    responseData = json.dumps(list_of_dicts)
    return HttpResponse(responseData, content_type="application/json")


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def room_list_chat(request):

    print("room_list_chat > is_authenticated = ", request.user.is_authenticated, " request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "room_list_chat"}

    if request.method != 'POST':
        return HttpResponseForbidden()

    room_name = json.loads(request.body)['room']
    room_instance = room.objects.get(name=room_name)
    print("room_list_chat > room_name=", room_name, "room_instance.id=", room_instance.id)

    # obtiene todos los mensajes de las sala especificada
    values = roomChat.objects.filter(room=room_instance).values('user__username','message')
    for value in values:
        print(value)

    # Convert the QuerySet to a List
    list_of_dicts = list(values)

    # Convert List of Dicts to JSON
    responseData = json.dumps(list_of_dicts)
    return HttpResponse(responseData, content_type="application/json")


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
#recibe como entrada "user_name" y devuelve todos los mensajes escritos por ese usuario hacia el usuario actual "request.user"
def user_list_chat(request):

    print("user_list_chat > is_authenticated = ", request.user.is_authenticated, " request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "user_list_chat"}

    if request.method != 'POST':
        return HttpResponseForbidden()

    user_name = json.loads(request.body)['user_name']
    user_instance = User.objects.get(username=user_name)

    content = {"message": "user_list_chat user_name=" + user_instance.username} # diccionario con formato JSON
    print("user_list_chat > user_name=" + user_instance.username)

    # obtiene todos los mensajes del usuario especificado hacia el usuario actual
    values = userChat.objects.filter(user=user_instance, user_destination=request.user.id).values('user__username','message')
    for value in values:
        print(value)

    # Convert the QuerySet to a List
    list_of_dicts = list(values)

    # Convert List of Dicts to JSON
    responseData = json.dumps(list_of_dicts)
    return HttpResponse(responseData, content_type="application/json")

