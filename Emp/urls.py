from django.urls import path
from Emp.views import empIndex,empStdIndex

urlpatterns = [
    path("Empn/",empIndex),
    path("EmpSeri/",empStdIndex),
]