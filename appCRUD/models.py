from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Livro(models.Model):
    # ID do livro no Google Books (para evitar duplicatas)
    google_books_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    
    # Campos do livro
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    capa_url = models.URLField(max_length=500, blank=True, null=True)
    
    # Campos que o usuário pode preencher
    nota = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True, blank=True
    )
    resenha = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
