#import django.contrib.auth.views
from django.urls import include, path
from rest_framework import routers
from . import views as myapi_views
from .views_games import game_create, game_delete, game_list
from .views_rooms import room_create, room_delete, room_in, room_out, room_list_users, room_list_chat, roomChat_create,\
    userChat_create, user_list_chat


router = routers.DefaultRouter()
router.register(r'users', myapi_views.userViewSet)    #vista para los usuarios de django
router.register(r'room', myapi_views.roomViewSet)
router.register(r'roomUser', myapi_views.roomUserViewSet)
router.register(r'game', myapi_views.gameViewSet)
router.register(r'roomChat', myapi_views.roomChatViewSet)
router.register(r'userChat', myapi_views.userChatViewSet)

urlpatterns = [
    path('', include(router.urls)), #monta en "http://xxx/zzz/" las rutas de la clases personalizada registradas en "router"
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #monta en "http://xxx/zzz/" las ruta/s del fichero "../venv/lib/site-packages/rest_framework/urls.py"

    path('welcome/', myapi_views.welcome), #monta en "http://xxx/welcome/" la ruta de la clase personalizada "welcome"

    path('game_create/', game_create),
    path('game_delete/', game_delete),
    path('game_list/', game_list),

    path('room_create/', room_create),
    path('room_delete/', room_delete),
    path('room_in/', room_in),
    path('room_out/', room_out),
    path('room_list_users/', room_list_users),
    path('room_list_chat/', room_list_chat),
    path('roomChat_create/', roomChat_create),
    path('userChat_create/', userChat_create),
    path('user_list_chat/', user_list_chat),

]