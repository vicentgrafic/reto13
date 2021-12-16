from .models import game
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
from django.db import IntegrityError
import json

@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def game_create(request):

    print("game_create > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "game_create Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    name = json.loads(request.body)['name']
    #maximum_players = json.loads(request.body)['maximum_players']

    content = {"message": "game_create a " + name} # diccionario con formato JSON
    print("game_create > name=", name)

    try:
        # crea un registro
        game.objects.create(name=name)
    except IntegrityError as e:
        print(e.args)
        return HttpResponseForbidden()

    return JsonResponse(content)

@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def game_delete(request):

    print("game_delete > is_authenticated = ", request.user.is_authenticated," request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "game_delete Error..."}

    if request.method != 'POST':
        return HttpResponseForbidden()

    game_name = json.loads(request.body)['name']
    try:
         game_instance = game.objects.get(name=game_name)
    except game.DoesNotExist:
        return HttpResponseForbidden()

    print("game_delete > game_instance.created_by = ", game_instance.name )

    content = {"message": "game_delete a " + game_name} # diccionario con formato JSON
    print("room_delete > game_name=", game_name, "game_instance.id=", game_instance.id)

    #borra el registro
    game_instance.delete()

    return JsonResponse(content)


@permission_classes([IsAuthenticated]) # solo puede acceder si está autentificado
@csrf_exempt # desactiva la seguridad csrf necesaria para POST con TOKEN
def game_list(request):

    print("game_list > is_authenticated = ", request.user.is_authenticated, " request.method =", request.method,",request.user.id =", request.user.id, ", request.user =", request.user)
    content = {"message": "game_list"}

    if request.method != 'POST':
        return HttpResponseForbidden()

    # gmaname = json.loads(request.body)['room']
    # room_instance = room.objects.get(name=room_name)
    # print("game_list > room_name=", room_name, "room_instance.id=", room_instance.id)

    # obtiene todos los mensajes de las sala especificada
    values = game.objects.all().values('name')
    for value in values:
        print(value)

    # Convert the QuerySet to a List
    list_of_dicts = list(values)

    # Convert List of Dicts to JSON
    responseData = json.dumps(list_of_dicts)
    return HttpResponse(responseData, content_type="application/json")