from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lot

@login_required(login_url='/login')
def BatchList(request):
    lot = Lot.objects.all().select_related('id_article').order_by('-lot')
    return render(request, 'batch_management/batchlist.html',
                  {'lot': lot})