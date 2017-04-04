from django.conf.urls import include, url
from django.contrib import admin
# import blog.views as bv

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
]
