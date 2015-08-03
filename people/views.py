from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from core.views import getCategories
from django.contrib.auth import authenticate,login,logout
from . import forms
# Create your views here.

def main(request):
	if(not(request.user.is_authenticated())):
		return redirect("/user/login/")

	return render(request,'people/user.html',{'category':getCategories()})


def loginView(request):
	if(request.method == 'POST'):
		form = forms.UserForm(request.POST)
	
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if(user is not None):
				login(request,user)
				return redirect('/user/')
	else:
		form = forms.UserForm()
		return render(request,'people/login.html',{'form':form,'category':getCategories()})

def logoutView(request):
	logout(request)
	return redirect('/')
