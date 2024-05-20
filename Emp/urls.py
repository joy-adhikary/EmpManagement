from django.urls import path
from Emp.views import empStdIndex,empApiviewClass,RegisterUser,LoginApi

urlpatterns = [
    path("EmpSeri/",empStdIndex),
    path('emp/',empApiviewClass.as_view()),
    path('regi/',RegisterUser.as_view()),
    path('log/',LoginApi.as_view()),

]