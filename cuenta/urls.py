from django.urls import path
from cuenta.views import registrar

urlpatterns = [
    path('registrar/', registrar ,name='registrar')
]
