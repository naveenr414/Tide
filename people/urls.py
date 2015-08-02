from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.main,name="main"),
	url(r'^login/$',views.login,name="login"),
]
