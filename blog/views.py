from django.shortcuts import render

# Create your views here.
#global setting
from my_blog import settings


def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'EMAIL':settings.EMAIL,
    }

def index(request):
    return render(request,'index.html',locals())