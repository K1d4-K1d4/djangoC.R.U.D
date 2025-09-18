from rest_framework import serializers
from .models import Livro


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'capa_url', 'nota', 'resenha']
        read_only_fields = ['id', 'autor', 'capa_url']


class EditarResenhaSerializer(serializers.Serializer):
    titulo = serializers.ChoiceField(choices=[], required=True)
    nota = serializers.IntegerField(required=False, min_value=0, max_value=10)
    autor = serializers.CharField(required=False, allow_blank=True)
    resenha = serializers.CharField(required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].choices = [
            (livro.titulo, livro.titulo) for livro in Livro.objects.all()
        ]
