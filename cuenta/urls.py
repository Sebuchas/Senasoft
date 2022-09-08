from django.urls import path
from cuenta.views import registrar

urlpatterns = [
    path('registrar/<int:pk>', registrar ,name='registrar'),
]
