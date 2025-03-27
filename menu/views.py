from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'homepage.html')
