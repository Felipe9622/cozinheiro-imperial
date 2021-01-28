from django.urls import path

from receitas import views

urlpatterns = [
    path('', views.index, name='index'),

    path('receitas/', views.ReceitaListView.as_view(), name='list'),
    path('receitas/<int:pk>', views.ReceitaDetailView.as_view(), name='detail'),
]