from django.urls import path,include

urlpatterns = [
    path("Adm/",include('Adm.urls')),
    path("Emp/",include('Emp.urls')),
]
