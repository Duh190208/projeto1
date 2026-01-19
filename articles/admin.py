from django.contrib import admin
from .models import Category, Author, Article

# Registra os modelos para aparecerem no painel de controle
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') # Mostra o nome e o slug na lista
    prepopulated_fields = {'slug': ('name',)} # Cria o slug automaticamente enquanto você digita o nome

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id') # Mostra o nome e o ID (UUID)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author') # Mostra título, categoria e autor na lista
    list_filter = ('category',) # Cria um filtro lateral por categoria