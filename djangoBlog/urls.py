"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,include,re_path
from blog import views as blog_views
from blog import views

import blog


from argparse import Namespace
from operator import index
from django.urls import path,re_path,include
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', blog_views.index),
    path('accounts/', include('allauth.urls')),  





    path('', blog.views.threelist_views5),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# 使用nigx部署的时候就不需要这么设置了，转发静态文件就可以了，只是调试的需要这么操作
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



