#coding:utf8
from django.shortcuts import render, redirect


# Create your views here.
from blog import models
from django.http import HttpResponse



import json

import requests
from bs4 import BeautifulSoup
from builtwith import builtwith

# Create your views here.
def index(request):
    id2 = models.Article.objects.get(id=2)
    print("id2:", id2)

    allarticle=models.Article.objects.all()
    print("allarticle,",allarticle)

    #content = ({'allarticle': allarticle})
    content={
        'allarticle':allarticle
            }
    return render(request, 'blog/index.html',locals())




