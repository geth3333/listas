#PARTE DE URLS LISTA

from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.producto, name='producto'),
)