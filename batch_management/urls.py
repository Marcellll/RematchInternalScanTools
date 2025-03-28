from django.urls import path
from .views import BatchList, BatchDetail, BatchUpdate, BatchNew, BatchAdd

urlpatterns = [
    path("", BatchList, name='batchlist'),
    path("<int:lot_id>/", BatchDetail, name='batchdetail'),
    path("update/<int:lot_id>/", BatchUpdate, name='batch_update'),
    path("add/", BatchNew, name='batch_new'),
    path("add/new", BatchAdd, name='batch_add'),
]
