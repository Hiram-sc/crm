from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('contatos/', views.contatos, name='contatos'),
    path('conversas/', views.contatos, name='conversas'),
    path('agenda/', views.agenda, name='agenda'),
    path('logout/', views.logout_view, name='logout')
]