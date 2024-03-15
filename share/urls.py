from django.urls import path
from .views import MyShareView, AddShareView, UpdateShareView, AllStockList, NewsView,ShareDeleteSlotView


urlpatterns: list = [
    path('', AllStockList.as_view(), name='all-shares'),
    path('mine', MyShareView.as_view(), name='mine'),
    path('add', AddShareView.as_view(), name='add-share'),
    path('update/<slug>', UpdateShareView.as_view(), name='update-share'),
    path('update/<slug>/slot/<int:slot_id>/', UpdateShareView.as_view(), name='update-slot-share'),
    path('update/<slug>/slot/<int:slot_id>/delete', ShareDeleteSlotView.as_view(), name='delete-slot-share'),
    path('news', NewsView.as_view(), name='news'),

]

