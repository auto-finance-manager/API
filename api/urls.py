from django.urls import path, include


urlpatterns: list = [
    path('share/', include('share.api.urls'))
]

