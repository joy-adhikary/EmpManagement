from django.urls import path
from Emp.views import empStdIndex,empApiviewClass

urlpatterns = [
    path("EmpSeri/",empStdIndex),
    path('emp/',empApiviewClass.as_view())
]