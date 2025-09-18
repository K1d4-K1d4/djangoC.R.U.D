from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def create(self, request, *args, **kwargs):
        titulo = request.data.get('titulo')
        nota = request.data.get('nota')
        resenha = request.data.get('resenha')

        # Validação do título
        if not titulo:
            return Response({'erro': 'O campo título é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        # Se nota não for enviada ou vier vazia, define como 0
        try:
            nota = int(nota) if nota not in (None, '') else 0
        except ValueError:
            return Response({'erro': 'Nota deve ser um número inteiro.'}, status=status.HTTP_400_BAD_REQUEST)

        # Busca na Google Books
        url = f'https://www.googleapis.com/books/v1/volumes?q={titulo}'
        try:
            resposta = requests.get(url)
            dados = resposta.json()
        except Exception:
            return Response({'erro': 'Erro ao consultar a API do Google Books.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not dados.get('items'):
            return Response({'erro': 'Livro não encontrado na API do Google Books.'}, status=status.HTTP_404_NOT_FOUND)

        info = dados['items'][0].get('volumeInfo', {})
        google_books_id = dados['items'][0].get('id', '')
        autor = ', '.join(info.get('authors', [])) if info.get('authors') else 'Autor desconhecido'
        capa_url = info.get('imageLinks', {}).get('thumbnail') if info.get('imageLinks') else None

        # Evita duplicatas
        if Livro.objects.filter(google_books_id=google_books_id).exists():
            return Response({'erro': 'Este livro já está cadastrado.'}, status=status.HTTP_400_BAD_REQUEST)

        # Cria o livro no banco
        livro = Livro.objects.create(
            google_books_id=google_books_id,
            titulo=info.get('title', titulo),
            autor=autor,
            capa_url=capa_url,
            nota=nota,
            resenha=resenha
        )

        return Response(LivroSerializer(livro).data, status=status.HTTP_201_CREATED)
