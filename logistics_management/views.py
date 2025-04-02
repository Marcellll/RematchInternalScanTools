from enum import Enum
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Chargement, Camion, ChargementStatus
from .forms import UpdateChargementForms, NewCamionForms

@login_required(login_url='/login')
def LogisticsOverview(request: HttpRequest) -> HttpResponse:
    chargement_ouvert = Chargement.objects.filter(status=ChargementStatus.OUVERT.value)
    return render(request, 'logistics_management/logistics_overview.html',
                  {'chargement' : chargement_ouvert})

@login_required(login_url='/login')
def LogisticsChargementCamion(request: HttpRequest, id_chargement: int) -> HttpResponse:
    chargement = Chargement.objects.get(id=id_chargement)
    camion = Camion.objects.filter(id_chargement=id_chargement).order_by('id')
    forms = UpdateChargementForms({'status_chargement': chargement.status,
                              'date_debut': chargement.date_debut,
                              'date_fin': chargement.date_fin})
    return render(request, 'logistics_management/logistics_chargement_camion.html',
                  { 'chargement': chargement,
                    'camion': camion,
                    'form' : forms})

@login_required(login_url='/login')
def LogisticsChargementUpdate(request: HttpRequest, id_chargement: int) -> HttpResponse:
    if request.method == 'POST':
        chargement = Chargement.objects.get(id=id_chargement)
        chargementforms = UpdateChargementForms(request.POST)
        if chargementforms.is_valid():
            chargement.status = chargementforms.cleaned_data['status_chargement']
            chargement.date_debut = chargementforms.cleaned_data['date_debut']
            chargement.date_fin = chargementforms.cleaned_data['date_fin']
            if chargement.date_debut > chargement.date_fin:
                messages.error(request, f"La date de début ne peut pas être après la date de fin")
                return LogisticsChargementCamion(request, id_chargement)
            chargement.save()
            messages.success(request, f"Chargement {chargement} modifié")
            return redirect('logistics_overview')
        messages.error(request, f"Une erreur est survenue {chargementforms.errors.as_text()}")
    return LogisticsChargementCamion(request, id_chargement)
        
@login_required(login_url='/login')
def LogisticsChargementFinished(request: HttpRequest) -> HttpResponse:
    chargement_termine = Chargement.objects.filter(status=ChargementStatus.TERMINE.value)
    return render(request, 'logistics_management/logistics_chargement_finished.html',
                  {'chargement' : chargement_termine})

@login_required(login_url='/login')
def LogisticsChargementCamionAdd(request: HttpRequest, id_chargement: int) -> HttpResponse:
    chargement = Chargement.objects.get(id=id_chargement)
    new_camion_forms = NewCamionForms()
    return render(request, 'logistics_management/logistics_chargement_camion_add.html',
                  {'form': new_camion_forms,
                   'chargement': chargement})

@login_required(login_url='/login')
def LogisticsChargementCamionNew(request: HttpRequest, id_chargement:int) -> HttpResponse:
    if request.method=='POST':
        new_camion_forms = NewCamionForms(request.POST)
        chargement = Chargement.objects.get(id=id_chargement)
        if new_camion_forms.is_valid():
            new_camion = Camion()
            new_camion.description = new_camion_forms.cleaned_data['description']
            new_camion.id_chargement = chargement
            new_camion.save()
            messages.success(request, f"Nouveau camion enregistré {new_camion}")
    return redirect('logistics_chargement_camion', id_chargement=id_chargement)

def LogisticsChargementDelete(request: HttpRequest, id_chargement:int, id_camion: int) -> HttpResponse:
    delete_camion = Camion.objects.get(id=id_camion)
    delete_camion.delete()
    messages.success(request, f"Camion: {delete_camion} a été supprimé")
    return redirect('logistics_chargement_camion', id_chargement=id_chargement)

