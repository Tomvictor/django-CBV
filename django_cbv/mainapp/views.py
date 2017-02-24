from django.shortcuts import render
from mainapp.models import Profile
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return render(request,'home.html',{})

class home_page(TemplateView):
    template_name = "home.html"