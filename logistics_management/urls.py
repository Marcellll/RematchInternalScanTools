from django.urls import path

from .views import (LogisticsOverview,
                    LogisticsChargementCamion,
                    LogisticsChargementUpdate,
                    LogisticsChargementFinished,
                    LogisticsChargementCamionAdd,
                    LogisticsChargementCamionNew,
                    LogisticsChargementDelete)

urlpatterns = [
    path("", LogisticsOverview, name="logistics_overview"),
    path("finished", LogisticsChargementFinished, name="logistics_chargement_finished"),
    path("<int:id_chargement>", LogisticsChargementCamion, name="logistics_chargement_camion"),
    path("<int:id_chargement>/add", LogisticsChargementCamionAdd, name="logistics_chargement_camion_add"),
    path("<int:id_chargement>/add/new", LogisticsChargementCamionNew, name="logistics_chargement_camion_new"),
    path("<int:id_chargement>/update", LogisticsChargementUpdate, name="logistics_chargement_update"),
    path("<int:id_chargement>/delete/<int:id_camion>", LogisticsChargementDelete, name="logistics_chargement_delete"),
]
