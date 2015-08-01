from django.shortcuts import render
from page.models import Category
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.

def main(request):
        template = loader.get_template("core/index.html")

	categoryList = Category.objects.all()

	#Make the list into a dictionary
	categoryDictionary = {}
	
	for i in categoryList:
		categoryDictionary[i.name] = i.color


        context = RequestContext(request,{'category':categoryDictionary})
        return HttpResponse(template.render(context))
 
