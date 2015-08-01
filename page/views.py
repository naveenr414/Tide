from django.shortcuts import render,get_object_or_404
from .models import Page
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.conf import settings
from . import models

# Create your views here.

def page(request,page_id):
	p = Page.objects.get(pk=page_id)
	title = p.title
	template = loader.get_template("page/page.html")

	#Load the Pages Markdown	
	markdown = settings.PROJECT_ROOT
	markdown = str(markdown).replace("/tide/settings","/static/pages/")
	markdown+=str(page_id)+".md"
	markdown = open(markdown).read()

	categoryObjects = models.Category.objects.all()
	categoryDictionary = {}
	for i in categoryObjects:
		categoryDictionary[i.name] = i.color
	
	context = RequestContext(request,{'title':"<h1> Joe </h1>","category":categoryDictionary})
	return HttpResponse(template.render(context))


