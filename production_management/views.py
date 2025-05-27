from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pdb
from .forms import CreateOFForms, UpdateOFForms, AddNomenclature
from .models import OrdreFabrication, StatusOF, ArticleParLot, Nomenclature

@login_required(login_url='/login')
def ProductionOverview(request: HttpRequest) -> HttpResponse:
    production_planifie = OrdreFabrication.objects.filter(status_of=StatusOF.PLANIFIE.value).order_by('date_debut')
    production_terminee = OrdreFabrication.objects.filter(status_of=StatusOF.TERMINE.value).order_by('-date_debut')
    return render(request, 'production_management/production_overview.html',
                  {
                      'of_planifie': production_planifie,
                      'of_termine' : production_terminee
                  })

@login_required(login_url='/login')
def ProductionNew(request: HttpRequest) -> HttpResponse:
    return render(request, 'production_management/production_add.html',
                    {'OFforms': CreateOFForms()})

@login_required(login_url='/login')
def ProductionAdd(request: HttpRequest) -> HttpResponse:
    newofforms = CreateOFForms(request.POST)
    if newofforms.is_valid():
        of = OrdreFabrication()
        of.id_lot = newofforms.cleaned_data['lot']
        of.date_debut = newofforms.cleaned_data['date_debut']
        of.date_fin = newofforms.cleaned_data['date_fin']
        of.status_of = StatusOF.PLANIFIE.value
        #Checking that the dates are set correctly
        if of.date_fin < of.date_debut:
            messages.error(request, f"La date de début ne peut pas être après la date de fin")
            return ProductionNew(request)
        #Check that the batch has a field type
        if of.id_lot.id_article == None:
            messages.error(request, f"Aucun type de d'article est rattaché au lot: {of.id_lot.lot}")
            return ProductionNew(request)
        of.save()
        #Create the bom after creating the OF
        nomenclature = Nomenclature.objects.filter(id_article=of.id_lot.id_article)
        for article in nomenclature:
            articleParLot = ArticleParLot()
            articleParLot.id_ordre_fabrication = of
            articleParLot.id_article = article.id_nomenclature
            articleParLot.save()
        messages.success(request, f"Ordre de fabrication pour le lot {of.id_lot.lot} a été crée")
        return redirect('production_overview')
    messages.error(request, f"Une erreur est survenue: {newofforms.errors.as_text()} ")
    return ProductionNew(request)

@login_required(login_url='/login')
def ProductionDetail(request: HttpRequest, id_of: int) -> HttpResponse:
    of = OrdreFabrication.objects.get(id=id_of)
    return render(request, 'production_management/production_detail.html',
                  {'of': of, 'offorms': UpdateOFForms({
                      'date_debut' : of.date_debut,
                      'date_fin' : of.date_fin,
                      'status_of' : of.status_of
                  })})

@login_required(login_url='/login')
def ProductionUpdate(request: HttpRequest, id_of:int) -> HttpResponse:
    of = OrdreFabrication.objects.get(id=id_of)
    if request.method == 'POST':
        batchforms = UpdateOFForms(request.POST)
        if batchforms.is_valid():
            of.date_debut = batchforms.cleaned_data['date_debut']
            of.date_fin = batchforms.cleaned_data['date_fin']
            of.status_of = batchforms.cleaned_data['status_of']
            of.save()
            messages.success(request, f"Ordre de fabrication modifié avec succès")
        else:
            messages.error(request, f"Ordre de fabrication non mis à jour")
    return redirect('production_overview')

@login_required(login_url='/login')
def ProductionNomenclature(request: HttpRequest, id_of: int) -> HttpResponse:
    articleParLot = ArticleParLot.objects.filter(id_ordre_fabrication=id_of).order_by('id_article__numero_article')
    of = OrdreFabrication.objects.get(id=id_of)
    form = AddNomenclature(request.POST, id_ordre_fabrication=id_of)
    return render(request, 'production_management/production_article.html',
                  {'article': articleParLot,
                   'of': of,
                   'form': form})

@login_required(login_url='/login')
def ProductionNomenclatureAdd(request: HttpRequest, id_of: int) -> HttpResponse:
    if request.method == 'POST':
        of = OrdreFabrication.objects.get(id=id_of)
        nomenclatureForm = AddNomenclature(request.POST)
        if nomenclatureForm.is_valid():
            of = OrdreFabrication.objects.get(id=id_of)
            articleParLot = ArticleParLot()
            articleParLot.id_ordre_fabrication = of
            articleParLot.id_article = nomenclatureForm.cleaned_data['article']
            articleParLot.save()
            messages.success(request, f"L'article {articleParLot.id_article} a été ajouté à l'ordre de fabrication pour le lot {of.id_lot.lot} - {of.id_lot.description}")
        else:
            messages.error(request, "Une erreur est survenue")
    return redirect('production_nomenclature', id_of=id_of)

@login_required(login_url='/login')
def ProductionNomenclatureDelete(request: HttpRequest, id_of: int, id_nomenclature: int) -> HttpResponse:
    articleParLot = ArticleParLot.objects.get(id=id_nomenclature)
    articleParLot.delete()
    return redirect('production_nomenclature', id_of=id_of) 
