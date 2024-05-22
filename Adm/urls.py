from django.urls import path,include
from Adm.views import admStdIndex,AdminClass,ModelViewSetExample

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'AdminMVS', ModelViewSetExample, basename='AdminMVS')
urlpatterns =  router.urls

urlpatterns = [
    # path("AdmSeri/",admStdIndex),
    path('', include(router.urls)),
    path("AdmSeri/",AdminClass.as_view())
]