from django.conf.urls import  url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$',views.index ),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name="article_page")
   
]
