from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def InventoryOverview(request: HttpRequest) -> HttpResponse:
    return render(request, 'inventory_management/inventory_overview.html')