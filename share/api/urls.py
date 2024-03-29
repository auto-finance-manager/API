from django.urls import path, include
from share.api import views

urlpatterns: list = [
    path('', views.AllSharesView.as_view()),
    path('mine/', views.MyShare.as_view()),
    path('sync/', views.ShareUpdateView.as_view()),
    path('news/', views.NewsView.as_view()),
]

