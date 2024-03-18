from django.urls import path, include


urlpatterns: list[path] = [
    path('share/', include('share.api.urls'))
]

