from django.urls import path
from book import views

urlpatterns = [
    path('',views.home, name= 'home' ),
    path('/autores', views.autores, name='autores'),
    path('/fale', views.fale, name='fale'),
]
