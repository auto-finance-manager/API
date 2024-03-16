from django.urls import path
from . import views


auth_patterns: list = [
    path('login', views.LoginView.as_view(), name='user_login'),
    path('logout', views.LogoutView.as_view(), name='user_logout'),
    path('register', views.RegisterView.as_view(), name='user_register'),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('set-password', views.UserSetPasswordView.as_view(), name='password_reset_confirm'),

]


urlpatterns: list = [

]

urlpatterns += auth_patterns

