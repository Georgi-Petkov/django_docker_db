from django.urls import path

from . import views


urlpatterns = [
    path("index", views.index, name='index'),
    path('get_quote', views.get_quote, name='get_quote'),
    path("id_quote", views.id_quote, name='id_quote')

]