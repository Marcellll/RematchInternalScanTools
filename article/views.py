from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Article, FrontBack
from .forms import ArticleForms

@login_required(login_url='/login')
def ArticleList(request: HttpRequest) -> HttpResponse:
    article = Article.objects.all().order_by('numero_article')
    return render(request, 'article/article_list.html', {'article': article})
    
@login_required(login_url='/login')
def ArticleNew(request: HttpRequest) -> HttpResponse:
    return render(request, 'article/article_add.html', 
                  {'form': ArticleForms()})

@login_required(login_url='/login')
def ArticleDetail(request: HttpRequest, id_article: int) -> HttpResponse:
    article = Article.objects.get(id=id_article)
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        if form.is_valid():
            article.numero_article = form.cleaned_data['numero_article']
            article.description_article = form.cleaned_data['description']
            article.front_back = form.cleaned_data['front_back']
            article.categorie = form.cleaned_data['categorie']
            if Article.objects.filter(numero_article=article.numero_article).exists():
                messages.warning(request, f"L'article {article.numero_article} existe déjà")
            article.save()
            messages.success(request, f"L'article {article.numero_article} - {article.description_article} a été modifié")
        return redirect('article_list')
    return render(request, 'article/article_detail.html', 
                  {'article': article, 'form': ArticleForms(
                        {'numero_article': article.numero_article,
                         'description': article.description_article,
                         #TODO:Check how to get the right key/value pair from the enum to not get the error message
                         'front_back': article.front_back,
                         'categorie': article.categorie}
                  )})

@login_required(login_url='/login')
def ArticleAdd(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        if form.is_valid():
            article = Article()
            article.numero_article = form.cleaned_data['numero_article']
            article.description_article = form.cleaned_data['description']
            article.front_back = form.cleaned_data['front_back']
            article.categorie = form.cleaned_data['categorie']
            if Article.objects.filter(numero_article=article.numero_article).exists():
                messages.error(request, f"L'article {article.numero_article} existe déjà")
                return redirect('article_new')
            article.save()
            messages.success(request, f"L'article {article.numero_article} - {article.description_article} a été crée")
    return redirect('article_list')