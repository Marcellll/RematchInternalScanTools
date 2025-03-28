from django.urls import path
from .views import BatchList, BatchDetail, BatchUpdate

urlpatterns = [
    path("", BatchList, name='batchlist'),
    path("<int:lot_id>/", BatchDetail, name='batchdetail'),
    path("update/<int:lot_id>/", BatchUpdate, name='batch_update')
]
