from django.urls import path
from .views import RerunList, RerunDetailList, DeleteRerun
#from .views import ReRunView, ReRunDetailView

urlpatterns = [
    path("", RerunList, name='re_run'),
    path("<int:id_of>/", RerunDetailList, name='re_run_order'),
    path("delete/<int:id_pesee>", DeleteRerun, name='delete_rerun'),
    #path("", ReRunView.as_view(), name="re_run"),
    #path("<int:of_id>/", ReRunDetailView.as_view(), name = "re_run_order"),
]
