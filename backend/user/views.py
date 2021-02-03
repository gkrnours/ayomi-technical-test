from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from django.shortcuts import render

from .forms import SigninForm

def index(request):
    return render(request, "user/home.html")


class SigninView(FormView):
    template_name = "user/signup.html"
    form_class = auth_forms.UserCreationForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    template_name = "user/login.html"
    success_url = "/"
    redirect_authenticated_user = True


# import AuthenticationForm, UserCreationForm