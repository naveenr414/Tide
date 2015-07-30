from django.shortcuts import render,get_object_or_404
from .models import Page
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.

def page(request,page_id):
	p = Page.objects.get(pk=page_id)
	title = p.title
	template = loader.get_template("page/page.html")
	context = RequestContext(request,{'title':title})
	return HttpResponse(template.render(context))


