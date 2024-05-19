from django.urls import path
from Emp.views import empStdIndex,empApiviewClass,RegisterUser

urlpatterns = [
    path("EmpSeri/",empStdIndex),
    path('emp/',empApiviewClass.as_view()),
    path('regi/',RegisterUser.as_view())
]