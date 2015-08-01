from django.shortcuts import render
from page.models import Category
from django.http import HttpResponse,Http404
from django.template import loader,RequestContext

# Create your views here.

def getCategories():
	categoryList = Category.objects.all()

	categoryDictionary = {}

	for i in categoryList:
		categoryDictionary[i.name] = i.color

	return categoryDictionary

def main(request):

        template = loader.get_template("core/index.html")

        context = RequestContext(request,{'category':getCategories()})
        return HttpResponse(template.render(context))

def category(request,category):
	
	if not(category.lower() in (name.lower() for name in getCategories())):
		raise Http404("Non Existent Category "+category)

	template = loader.get_template("core/category.html")

	context = RequestContext(request,{'category':getCategories(),'currentCategory':category.capitalize()})

	return HttpResponse(template.render(context))
