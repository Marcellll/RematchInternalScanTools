from django.urls import path
from .views import ProductionOverview

urlpatterns = [
    path("", ProductionOverview, name="production_overview")
]
