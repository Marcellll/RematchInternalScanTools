from django.urls import path
from .views import (ProductionOverview, 
                    ProductionNew, 
                    ProductionAdd, 
                    ProductionDetail, 
                    ProductionUpdate,
                    ProductionNomenclature,
                    ProductionNomenclatureAdd,
                    ProductionNomenclatureDelete)

urlpatterns = [
    path("", ProductionOverview, name="production_overview"),
    path('add/', ProductionNew, name="production_new"),
    path('add/new', ProductionAdd, name="production_add"),
    path("<int:id_of>", ProductionDetail, name="production_detail"),
    path("<int:id_of>/update", ProductionUpdate, name="production_update"),
    path("<int:id_of>/article", ProductionNomenclature, name="production_nomenclature"),
    path("<int:id_of>/article/add", ProductionNomenclatureAdd, name="production_nomenclature_add"),
    path("<int:id_of>/article/delete/<int:id_nomenclature>", ProductionNomenclatureDelete, name="production_nomenclature_delete"),
]
