from django.urls import path
from .views import ArticleList, ArticleNew, ArticleAdd, ArticleDetail

urlpatterns = [
    path('', ArticleList, name='article_list'),
    path('<int:id_article>/', ArticleDetail, name='article_detail'),
    path('add/', ArticleNew, name='article_new'),
    path("add/new", ArticleAdd, name='article_add'),
]
