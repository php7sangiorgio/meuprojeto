from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscrevase_view, name='inscrevase'),
]