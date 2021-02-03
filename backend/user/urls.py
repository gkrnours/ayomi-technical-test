from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('info/', views.UpdateInfoView.as_view(), name='info'),
]