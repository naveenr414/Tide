from django.conf.urls import url,include

from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^page/',include('page.urls')),
	url(r'^$',views.main,name="main"),
]
