"""
URL configuration for certipuce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from events import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base),
    path("index/", views.index),
    path("procesar_login/", views.procesar_login, name="pl"),
    path("actualizar_datos/", views.actualizar_datos, name="ad"),
    path("index_admin/", views.index_admin, name="ia"),
    path("crear_evento/", views.crear_evento, name="ce"),
    path("crear_usuario/", views.crear_usuario, name="cu"),
    path("recuperar_contraseña/", views.recuperar_contraseña, name="rc"),
    path("admin_participantes/", views.admin_participantes, name="ap"),
    path("cerrar_cesion/", views.cerrar_cesion, name="cc"),
]
