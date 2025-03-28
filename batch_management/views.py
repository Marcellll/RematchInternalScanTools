from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lot
from .forms import BatchForms

@login_required(login_url='/login')
def BatchList(request: HttpRequest) -> HttpResponse:
    lot = Lot.objects.all().select_related('id_article').order_by('-lot')
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