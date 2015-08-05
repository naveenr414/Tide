from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.main,name="main"),
	url(r'^login/$',views.loginView,name="login"),
	url(r'^logout/$',views.logoutView,name="logout"),
	url(r'^new/$',views.newUser,name="new")
]
