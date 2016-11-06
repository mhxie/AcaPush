from django.conf.urls import url
from django.contrib import admin
from myproject.views import news
from myproject.views import notice
from myproject.views import comments
from myproject.views import search

urlpatterns = [
	url(r'^admin/$', admin.site.urls),

	url(r'^news/(\d{2})/(\d{8})/$', news, name='news'), #return the news of different academy before the date(00 or 00000000 will return all)

	url(r'^notice/(\d{2})/(\d{8})/$', notice, name='notice'), #return the notice of different academy before the date(00 or 00000000 will return all)
	
	
	url(r'^comments/(\d{2})/$', comments, name='comments'), #return the news of different academy
	url(r'^comments/upload/$', comments, name='comments'), #upload the comments to the server

	url(r'^search/(\d{1})/(\w{1,15})/(\d{2})/(\d{8})/$', search_news, name='search'), #search the news or notice(flag==0 or flag==1) with keyword（w{1,15}) (00 or 00000000 will return all academy and date news)

]

