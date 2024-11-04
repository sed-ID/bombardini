from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(next_page='core:login'), name='logout'),
]
