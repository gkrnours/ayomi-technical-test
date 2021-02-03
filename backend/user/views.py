from django.views.generic.edit import FormView
from django.shortcuts import render

from .forms import SigninForm

def index(request):
    return render(request, "user/home.html")


class SigninView(FormView):
    template_name = "signin.html"
    form_class = SigninForm
    success_url = "index.html"
    
    def form_valid(self, form):
        return super().form_valid(form)