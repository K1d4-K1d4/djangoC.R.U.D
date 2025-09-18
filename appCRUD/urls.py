from django.urls import path
from .views import (
    LivroList,
    BuscarLivroGoogle,
    AdicionarLivro,
    EditarLivro,
    ExcluirLivro,
)

urlpatterns = [
    # Listar livros cadastrados
    path('livros/', LivroList.as_view(), name='listar_livros'),

    # Buscar livros na API do Google Books
    path('livros/buscar/', BuscarLivroGoogle.as_view(), name='buscar_livro_google'),

    # Adicionar livro ao banco
    path('livros/adicionar/', AdicionarLivro.as_view(), name='adicionar_livro'),

    # Editar livro (passa o id do livro)
    path('livros/<int:livro_id>/editar/', EditarLivro.as_view(), name='editar_livro'),

    # Excluir livro (passa o id do livro)
    path('livros/<int:livro_id>/excluir/', ExcluirLivro.as_view(), name='excluir_livro'),
]