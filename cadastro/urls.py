from django.urls import path
from .views import cadastros, cadastrar, detalhe, editar, excluir

urlpatterns = [
    path('', cadastros, name='cadastros'),
    path('novo_cadastro/', cadastrar, name='novo_cadastro'),
    path('detalhe/<int:id_pessoa>', detalhe, name='detalhe_cadastro'),
    path('<int:id_pessoa>', editar, name='editar_cadastro'),
    path('excluir/<int:id_pessoa>', excluir, name='excluir_cadastro'),
]