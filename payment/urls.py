from django.urls import path
from .views import payment, thank_you

urlpatterns = [
    path('payment/', payment, name='payment'),
    path('thank-you/', thank_you, name='thank_you'),
]