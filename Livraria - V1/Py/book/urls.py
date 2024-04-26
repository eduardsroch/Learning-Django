from django.urls import path
from book import views

urlpatterns = [
    path('',views.home, name= 'home' ),
    path('autores/', views.autores, name='autores'),
    path('fale/', views.fale, name='fale'),
    path('imprensa/', views.imprensa, name='imprensa'),
    path('sobre/', views.sobre, name='sobre'),
    path('titulos/', views.titulos, name='titulos'),
    path('professor/', views.professor, name='professor'),
    path('abouteditora/', views.abouteditora, name='abouteditora'),
    path('form/', views.form, name='form'),
    path('carrinho/<id>', views.carrinho, name='carrinho'),
    path('busca/', views.busca, name='busca'),
    path('login/', views.login, name='login'),
]
