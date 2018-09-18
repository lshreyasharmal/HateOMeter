from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	url(r'^$', csrf_exempt(views.dataList.as_view()), name="restView"),
	url(r'^index/$', views.index, name='index'),
]
