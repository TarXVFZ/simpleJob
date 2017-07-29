from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index_find"),
	url(r'^find/$', views.find, name="find"),
]