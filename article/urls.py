from django.urls import path
from .views import ArticleList, ArticleNew, ArticleAdd, ArticleDetail, ArticleNomenclature, ArticleNomenclatureDelete, ArticleNomenclatureAdd

urlpatterns = [
    path('', ArticleList, name='article_list'),
    path('<int:id_article>/', ArticleDetail, name='article_detail'),
    path('<int:id_article>/nomenclature', ArticleNomenclature, name='article_nomenclature'),
    path("<int:id_article>/nomenclature/add/", ArticleNomenclatureAdd, name="article_nomenclature_add"),
    path("<int:id_article>/nomenclature/delete/<int:id_nomenclature>", ArticleNomenclatureDelete, name="article_nomenclature_delete"),
    path('add/', ArticleNew, name='article_new'),
    path("add/new", ArticleAdd, name='article_add'),
]
