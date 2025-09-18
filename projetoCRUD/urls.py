from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appCRUD.views import LivroViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livro')

urlpatterns = [
    path('', include(router.urls)),
    # Removido include('appCRUD.urls') se ele só servia para editar-resenha
    path('admin/', admin.site.urls),
]
