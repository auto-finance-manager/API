from django.urls import path
from .views import MyShareView, AddShareView


urlpatterns: list = [
    path('mine', MyShareView.as_view(), name='mine'),
    path('add', AddShareView.as_view(), name='add-share'),
]

