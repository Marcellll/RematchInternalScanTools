from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lot
from .forms import BatchForms, NewBatchForms

@login_required(login_url='/login')
def BatchList(request: HttpRequest) -> HttpResponse:
    lot = Lot.objects.all().select_related('id_article').order_by('-id')
    return render(request, 'batch_management/batchlist.html',
                  {'lot': lot})

@login_required(login_url='/login')
def BatchDetail(request: HttpRequest, lot_id: int) -> HttpResponse:
    lot = Lot.objects.get(id=lot_id)
    batchforms = BatchForms({
        'description': lot.description,
        'article': lot.id_article.description_article if lot.id_article != None else ""
    })
    return render(request, 'batch_management/batch_detail.html', 
                  {'lot': lot, 'batchforms': batchforms})

@login_required(login_url='/login')
def BatchUpdate(request: HttpRequest, lot_id: int) -> HttpResponse:
    lot = Lot.objects.get(id=lot_id)
    if request.method == 'POST':
        batchforms = BatchForms(request.POST)
        if batchforms.is_valid():
            lot.description = batchforms.cleaned_data['description']
            lot.id_article = batchforms.cleaned_data['article']
            lot.save()
    return render(request, 'batch_management/batch_detail.html', 
                  {'lot': lot, 'batchforms': batchforms})

@login_required(login_url='/login')
def BatchNew(request: HttpRequest) -> HttpResponse:
    return render(request, 'batch_management/batch_add.html',
                  {'newbatchforms': NewBatchForms()})

@login_required(login_url='/login')
def BatchAdd(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        newbatchforms = NewBatchForms(request.POST)
        if newbatchforms.is_valid():
            if Lot.objects.filter(lot=newbatchforms.cleaned_data['lot']).exists():
                messages.error(request, f"Lot {newbatchforms.cleaned_data['lot']} existe déjà")
                return redirect('batch_new')
            lot = Lot()
            lot.lot = newbatchforms.cleaned_data['lot']
            lot.description = newbatchforms.cleaned_data['description']
            lot.id_article = newbatchforms.cleaned_data['article']
            lot.save()
            messages.success(request, f"Lot {lot.lot} a été crée")
    return redirect('batchlist')
