from django.conf.urls import url,include

from django.views.generic import TemplateView
from . import views



urlpatterns = [
	url(r'^user/',include('people.urls')),
	url(r'^page/',include('page.urls')),
	url(r'^$',views.main,name="main"),
	url(r'^(?P<category>.+)/$',views.category,name="category")
]
