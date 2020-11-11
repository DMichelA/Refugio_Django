from django.urls import path,include

from apps.adopcion.views import index_adopcion

urlpatterns = [
    path('index/', index_adopcion, name="adopcion"),
]