from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = [
            'id',
            'titulo',
            'autor',
            'capa_url',
            'nota',
            'resenha'
        ]
        read_only_fields = ['id', 'autor', 'capa_url']
