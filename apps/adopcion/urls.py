from django.urls import path,include

from apps.adopcion.views import SolicitudList, SolicitudCreate

urlpatterns = [
    path('solicitud/listar/', SolicitudList.as_view(), name="solicitud_listar"),
    path('solicitud/nueva/', SolicitudCreate.as_view(), name="solicitud_crear"),
]