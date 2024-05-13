from django.urls import path
from Adm.views import admStdIndex,AdminClass

urlpatterns = [
    # path("AdmSeri/",admStdIndex)
    path("AdmSeri/",AdminClass.as_view())
]