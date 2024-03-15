from django.urls import path
from .views import MyShareView, AddShareView, UpdateShareView


urlpatterns: list = [
    path('mine', MyShareView.as_view(), name='mine'),
    path('add', AddShareView.as_view(), name='add-share'),
    path('update/<slug>', UpdateShareView.as_view(), name='update-share')
]

