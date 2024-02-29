from django.urls import path, include
from share.api import views

urlpatterns: list = [
    path('', views.AllSharesView.as_view())
]

