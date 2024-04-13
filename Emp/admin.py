from django.contrib import admin
from .models import Emp,LinkEmpWithAdmin

# Register your models here.
admin.site.register(Emp)
admin.site.register(LinkEmpWithAdmin)