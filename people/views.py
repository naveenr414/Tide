from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader,RequestContext
from core.views import getCategories

# Create your views here.

def main(request):
	if(not(request.user.is_authenticated())):
		return redirect("/user/login/")

	return HttpResponse(str(request.user.is_authenticated()))

def login(request):
	template = loader.get_template("people/login.html")
	context = RequestContext(request,{"category":getCategories()})

	return HttpResponse(template.render(context))
