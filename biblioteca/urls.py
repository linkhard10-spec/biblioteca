from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('marcar_lido/<int:id>/', views.marcar_lido, name='marcar_lido'),
    path('remover/<int:id>/', views.remover_livro, name='remover_livro'),
]
