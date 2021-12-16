"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    #monta en "http://xxx/admin/" las rutas de la clase "admin"
    path('', include('myapi.urls')),    #monta en "http://xxx/zzz/" las ruta/s personalizada/s del fichero "../myapy/urls.py"
    path('', include('rest_auth.urls')),#monta en "http://xxx/zzz/" las ruta/s del fichero "../venv/lib/site-packages/rest_auth/urls.py"
    path('registration/', include('rest_auth.registration.urls')),  #monta en "http://xxx/registration/" las ruta/s del fichero "../venv/lib/site-packages/rest_auth/urls/registration.urls"
]

'''URLS contenidas en ".../rest_auth/urls.py":
http://127.0.0.1:8000/registration/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/logout/
http://127.0.0.1:8000/user/
http://127.0.0.1:8000/password/change/
http://127.0.0.1:8000/password/reset/
http://127.0.0.1:8000/password/reset/confirm/
'''