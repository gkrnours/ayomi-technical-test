from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render

from .forms import UpdateInfoForm

def index(request):
    form = UpdateInfoForm()
    return render(request, "user/home.html")


class SigninView(FormView):
    template_name = "user/signup.html"
    form_class = auth_forms.UserCreationForm
    success_url = "/"

    def get_template_names(self):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return ["bs5_form.html"]
        else:
            return [""]
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    template_name = "user/login.html"
    success_url = "/"
    redirect_authenticated_user = True


class UpdateInfoView(UpdateView):
    template_name = "user/info.html"
    form_class = UpdateInfoForm
    success_url = "/"

    def is_ajax(self):
        return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get_template_names(self):
        if self.is_ajax():
            return ["bs5_form.html"]
        else:
            return ["user/info.html"]

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)