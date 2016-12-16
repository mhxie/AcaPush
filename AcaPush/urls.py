
"""newspush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from newspush.views import commit_comment
from newspush.views import fetch_comments
from newspush.views import login, logout
from newspush.views import fetch_news
from newspush.views import fetch_notice
from newspush.views import fetch_news
from newspush.views import search_news
from newspush.views import search_notice
from newspush.views import fetch_new_news,fetch_new_notice


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^comments/commit/(\d+)/(\d+)/$', commit_comment, name='commit_comment'), #upload the comments to the server
    url(r'^comments/(\d+)/$', fetch_comments, name='fetch_comments'), #return the news of different academy
    url(r'^login/$',login,name='login'),
    url(r'^logout/(\d+)/$',logout,name='logout'),
	url(r'^news/(\d+)/(\d{8})/$', fetch_news, name='fetch_news'), #return the news of different academy and date
	url(r'^notice/(\d+)/(\d{8})/$', fetch_notice, name='fetch_notice'), #return the notice of different academy and date
	url(r'^search_news/(\d+)/(\w{1,15})/$', search_news, name='search_news'), #search the news or notice with keyword（w{1,15})
    url(r'^search_notice/(\d+)/(\w{1,15})/$', search_notice, name='search_notice'),
	url(r'^new_news/(\d+)/(\d+)/$',fetch_new_news,name='fetch_new_news'),
	url(r'^new_notice/(\d+)/(\d+)/$',fetch_new_notice,name='fetch_new_notice'),
]
