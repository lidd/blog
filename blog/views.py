from django.shortcuts import render
# Create your views here.
# global setting
from my_blog import settings


def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'EMAIL': settings.EMAIL,
    }


def index(request):
    return render(request, 'index.html', locals())

def blog(request):
    return render(request,'full-width.html',locals())

def about(request):
    return render(request, 'about.html', locals())


def contact(request):
    return render(request,'contact.html',locals())


def single(request):
    return render(request,'single.html',locals())
