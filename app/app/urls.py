from django.contrib import admin
from django.urls import path

from main.views import AddressCreate, AddressValidate

urlpatterns = [
    path('address/validate/', AddressValidate.as_view()),
    path('address/create/', AddressCreate.as_view({'post': 'create'})),
    path('admin/', admin.site.urls),
]
