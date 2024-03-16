from django.urls import path
from . import views


auth_patterns: list = [
    path('login', views.LoginView.as_view(), name='user_login'),
    path('logout', views.LogoutView.as_view(), name='user_logout'),
    path('register', views.RegisterView.as_view(), name='user_register')
]


urlpatterns: list = [

]

urlpatterns += auth_patterns

