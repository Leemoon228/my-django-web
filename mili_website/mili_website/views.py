from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')
def blog(request):
        return render(request, 'blog.html')
def works(request):
        return render(request, 'works.html')
def lyrics(request):
        return render(request, 'lyrics.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
