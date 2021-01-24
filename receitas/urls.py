from django.urls import path

from receitas import views

app_name='receitas'
urlpatterns = [
    path('', views.home, name='home'),
]
