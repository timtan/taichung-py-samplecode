from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^traditional/$', views.csrf_exempt_dummy,  {'template_name': 'traditional_form.html'}, name='traditional'),
    url(r'^with_csrf/$', views.dummy,  {'template_name': 'csrf_form.html'}, name='with_csrf'),
    url(r'^other/$', TemplateView.as_view(template_name='other.html'), name='other'),
    url(r'^easier_form/$', views.easier_form),
    url(r'^crispy_form/$', views.easier_form, {'template_name': 'crispy_form.html'}),
    url(r'^model_form/$', views.model_form, {'template_name': 'crispy_form.html'}),
]
