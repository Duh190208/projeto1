import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from articles.models import Category, Author, Article

def popular():
    print("Cadastrando dados de teste...")

    # 1. Cria Categoria
    cat, created = Category.objects.get_or_create(
        slug="tecnologia",
        defaults={'name': 'Tecnologia'}
    )
    print(f"Categoria: {cat.name} {'(criada)' if created else '(já existia)'}")

    # 2. Cria Autor
    autor, created = Author.objects.get_or_create(
        name="Seu Nome",
        defaults={
            'picture': 'https://api.dicebear.com/7.x/avataaars/svg?seed=Felix'
        }
    )
    print(f"Autor: {autor.name} {'(criado)' if created else '(já existia)'}")

    # 3. Cria Artigo 1
    art1, created = Article.objects.get_or_create(
        title="O Futuro do Python",
        defaults={
            'summary': 'Um resumo sobre como o Python está dominando o mundo.',
            'first_paragraph': '<p>Este é o primeiro parágrafo visível para todos.</p>',
            'body': '<div><p>Este é o corpo secreto que só logados veem.</p></div>',
            'author': autor,
            'category': cat
        }
    )
    print(f"Artigo 1: {art1.title} {'(criado)' if created else '(já existia)'}")

    # 4. Cria Artigo 2
    art2, created = Article.objects.get_or_create(
        title="Django e Docker",
        defaults={
            'summary': 'Aprenda a usar containers com o framework mais famoso.',
            'first_paragraph': '<p>Docker facilita muito o deploy.</p>',
            'body': '<div><p>Conteúdo exclusivo para membros da plataforma.</p></div>',
            'author': autor,
            'category': cat
        }
    )
    print(f"Artigo 2: {art2.title} {'(criado)' if created else '(já existia)'}")

    print("\nDados cadastrados com sucesso!")
    print(f"Total de artigos: {Article.objects.count()}")

if __name__ == '__main__':
    popular()