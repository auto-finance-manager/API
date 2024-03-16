from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, RedirectView, TemplateView
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('all-shares'))
        return super(LoginView, self).get(*args, **kwargs)

    def get_success_url(self):
        return reverse('all-shares')

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if user := authenticate(username=username, password=password):
                if user.is_active:
                    login(request, user)
            else:
                raise self.form_invalid(form)

        return super(LoginView, self).post(request, *args, **kwargs)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('home_page')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('all-shares'))
        return super(RegisterView, self).get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        super(RegisterView, self).post(request, *args, **kwargs)


class LogoutView(RedirectView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')

