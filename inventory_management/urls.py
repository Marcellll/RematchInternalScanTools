from django.urls import path
from .views import InventoryOverview

urlpatterns = [
    path("", InventoryOverview, name="logistics_overview"),
]