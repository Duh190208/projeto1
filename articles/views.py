from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleListView(generics.ListAPIView):
    """
    Lista todos os artigos.
    Permite filtrar por categoria via URL: /api/articles/?category=slug
    """
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Article.objects.select_related('author', 'category').all()
        category_slug = self.request.query_params.get('category')
        
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        return queryset


class ArticleDetailView(generics.RetrieveAPIView):
    """
    Mostra detalhes de um artigo específico.
    A lógica de esconder o 'body' está no Serializer
    """
    queryset = Article.objects.select_related('author', 'category').all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [permissions.AllowAny]


class SignUpView(APIView):
    """
    Cadastro de novos usuários
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Username e password são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Usuário já existe'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password)
        return Response(
            {'message': 'Usuário criado com sucesso!', 'username': user.username},
            status=status.HTTP_201_CREATED
        )