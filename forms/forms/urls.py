from django.conf.urls import patterns, include, url
from django.contrib import admin
import demo.urls
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^', include(demo.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'admin/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout')

]
