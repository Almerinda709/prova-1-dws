from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.index, name='index'),
    ]
