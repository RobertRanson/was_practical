from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import loader

def index(request):
    latest_article_list = Article.objects.order_by('-publish_date')[:5]
    template = loader.get_template('news/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.

