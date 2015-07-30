from django.conf.urls import url,include

from django.views.generic import TemplateView

urlpatterns = [
	url(r'^page/',include('page.urls')),
	url(r'^$',TemplateView.as_view(template_name="core/index.html")),
]
