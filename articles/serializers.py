from rest_framework import serializers
from .models import Author, Category, Article

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'picture'] # Formato exato do JSON pedido

class ArticleListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary'] # Campos da lista geral

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    
    class Meta:
        model = Article
        # Começamos com os campos que todos podem ver
        fields = ['id', 'author', 'category', 'title', 'summary', 'first_paragraph', 'body']

    def to_representation(self, instance):
        """Lógica para esconder o 'body' se o utilizador não estiver logado"""
        representation = super().to_representation(instance)
        request = self.context.get('request')
        
        # Se o utilizador NÃO estiver autenticado, removemos o campo 'body'
        if request and not request.user.is_authenticated:
            representation.pop('body', None)
            
        return representation
