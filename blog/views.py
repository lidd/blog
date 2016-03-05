import logging
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

from django.shortcuts import render

# Create your views here.
# global setting
from blog.models import ARTICLE, CATEGORY
from my_blog import settings

logger = logging.getLogger('blog.views')


def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'EMAIL': settings.EMAIL,
    }


def index(request):
    try:
        category_list = CATEGORY.objects.all()
        article_list = ARTICLE.objects.all()
        paginator = Paginator(article_list,10)
        try:
            page_num = request.GET.get('page',1)
            article_list = paginator.page(page_num)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error('query db failed!',e)
    return render(request, 'index.html', locals())


def blog(request):
    return render(request, 'full-width.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())


def single(request):
    return render(request, 'single.html', locals())


def get_category(request, id):
    category_list = CATEGORY.objects.get(id)
    return render(request, 'index.html', locals())
