from Adm.views import index
from Emp.views import Empindex,EmIndexWithSerializer
from django.urls import path

urlpatterns = [
    path("Adm/",index),
    path("Emp/",Empindex),
    path("EmpSeri/",EmIndexWithSerializer),
]