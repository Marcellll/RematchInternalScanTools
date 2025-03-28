from django.urls import path
from .views import BatchList

urlpatterns = [
    path("", BatchList, name='batchlist'),
]
