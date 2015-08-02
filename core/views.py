from django.shortcuts import render
from page.models import Category,Page
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

	topStories = Page.objects.order_by("time")[:5]
	storyDictionary = {}
	for i in topStories:
		storyDictionary[i.title] = i.id

        template = loader.get_template("core/index.html")

        context = RequestContext(request,{'category':getCategories(),"stories":storyDictionary})
        return HttpResponse(template.render(context))

def category(request,category):
	
	if not(category.lower() in (name.lower() for name in getCategories())):
		raise Http404("Non Existent Category "+category)

	template = loader.get_template("core/category.html")

	categoryId = Category.objects.all().filter(name=category)[0].id
	pageList = list(Page.objects.all().filter(category=categoryId))
	pageDictionary = {}
	for i in pageList:
		pageDictionary[i.title] = i.id

	context = RequestContext(request,{'pageList':pageDictionary,'category':getCategories(),'currentCategory':category})

	return HttpResponse(template.render(context))
