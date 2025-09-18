from django.urls import path
from .views import consulta_livro

urlpatterns = [
    path('consultar/', consulta_livro, name='consultar-livro'),
]
