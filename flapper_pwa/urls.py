"""flapper_pwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from article import views

urlpatterns = [
    url('', include('pwa.urls')),
    url(r'^admin/', admin.site.urls),

    #url('', include('pwa.urls')),
    #url('', include('pwa.urls')),
    url(r'^$', views.index, name='home'),
    #url(r'^home/$', views.index, name='home'),
    #url(r'^$', views.index, name='home'),

    #url('base_layout', views.base_layout, name='base'),
    #url('/base_layout', views.base_layout, name='base'),

    url(r'^login/$', auth_views.login, {'template_name': 'articles/login.html'}, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^changepassword/$', views.change_password, name='change_password'),
    url(r'^account/userdetails/$', views.user_details, name='user_details'),
    url(r'^article/(?P<id_article>[0-9]+)/$', views.article_view, name='article_view')
]
