from django.urls import path
from Emp.views import empStdIndex

urlpatterns = [
    path("EmpSeri/",empStdIndex),
]