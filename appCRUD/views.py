from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializer import LivroSerializer
import requests

# Listar livros cadastrados
class LivroList(APIView):
    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

# Buscar livro na API externa (Google Books)
class BuscarLivroGoogle(APIView):
    def get(self, request):
        termo = request.query_params.get('termo')
        if not termo:
            return Response({'erro': 'Informe o termo de busca.'}, status=status.HTTP_400_BAD_REQUEST)
        url = f'https://www.googleapis.com/books/v1/volumes?q={termo}'
        resposta = requests.get(url)
        dados = resposta.json()
        livros_api = []
        for item in dados.get('items', []):
            info = item['volumeInfo']
            livros_api.append({
                'google_books_id': item['id'],
                'titulo': info.get('title', ''),
                'autor': ', '.join(info.get('authors', [])),
                'capa_url': info.get('imageLinks', {}).get('thumbnail', ''),
            })
        return Response(livros_api)

# Adicionar livro ao banco
class AdicionarLivro(APIView):
    def post(self, request):
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Editar livro
class EditarLivro(APIView):
    def put(self, request, livro_id):
        try:
            livro = Livro.objects.get(id=livro_id)
        except Livro.DoesNotExist:
            return Response({'erro': 'Livro não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LivroSerializer(livro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Excluir livro
class ExcluirLivro(APIView):
    def delete(self, request, livro_id):
        try:
            livro = Livro.objects.get(id=livro_id)
        except Livro.DoesNotExist:
            return Response({'erro': 'Livro não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)