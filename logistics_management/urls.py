from django.urls import path

from .views import LogisticsOverview

urlpatterns = [
    path("", LogisticsOverview, name="logistics_overview"),
]
