from django.urls import path
from .views import ArticleListView, ArticleDetailView, SignUpView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<uuid:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
