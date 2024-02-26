from django.urls import path
from Adm.views import admIndex,admStdIndex

urlpatterns = [
    path("Admn/",admIndex),
    path("AdmSeri/",admStdIndex),
]