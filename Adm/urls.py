from django.urls import path
from Adm.views import admStdIndex

urlpatterns = [
    path("AdmSeri/",admStdIndex)
]