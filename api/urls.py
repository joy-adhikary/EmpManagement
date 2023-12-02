from Adm.views import index
from Emp.views import Empindex
from django.urls import path

urlpatterns = [
    path("Adm/",index),
    path("Emp/",Empindex),
]