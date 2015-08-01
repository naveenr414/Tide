from django.conf.urls import url

from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
#	url(r'^$',TemplateView.as_view(template_name="page/page.html")),
	url(r'^(?P<page_id>[0-9]+)/$',views.page,name="page"),
	url(r'^$',views.main,name="main"),
]
