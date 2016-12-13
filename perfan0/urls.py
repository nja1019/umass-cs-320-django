from django.conf.urls import url

from . import views

app_name = 'perfan0'
urlpatterns = [
	# ex: /perfan0/
    url(r'^$', views.index, name='index'),
    # ex: /perfan/5/
    url(r'^(?P<system_id>[0-9]+)/$', views.detail, name='detail'),
]