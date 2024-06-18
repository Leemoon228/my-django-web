"""
URL configuration for mili_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
      
    # Django Auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/profile/', views.ProfileView.as_view() , name="profile"),


    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('index.html', TemplateView.as_view(template_name="index.html"), name="index"),
    path('AX2021.html', TemplateView.as_view(template_name="AX2021.html"), name="AX2021"),
    path('blog.html', TemplateView.as_view(template_name="blog.html"), name="blog"),
    path('gunner.html', TemplateView.as_view(template_name="gunner.html"), name="gunner"),
    path('key-ing.html', TemplateView.as_view(template_name="key-ing.html"), name="key-ing"),
    path('library.html', TemplateView.as_view(template_name="library.html"), name="library"),
    path('lyrics.html', TemplateView.as_view(template_name="lyrics.html"), name="lyrics"),
    path('mag-mell.html', TemplateView.as_view(template_name="mag-mell.html"), name="mag-mell"),
    path('miracle.html', TemplateView.as_view(template_name="miracle.html"), name="miracle"),
    path('pictures.html', TemplateView.as_view(template_name="pictures.html"), name="pictures"),
    path('pyrcone.html', TemplateView.as_view(template_name="pyrcone.html"), name="pyrcone"),
    path('works.html', TemplateView.as_view(template_name="works.html"), name="works"),
  
]
