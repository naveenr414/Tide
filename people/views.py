from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from core.views import getCategories
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Permission,Group
from django.db.models import Q
from . import forms
from page.models import Page
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def writer(request):
	return render(request,'people/writer.html',{'category':getCategories})

def main(request):
	if(not(request.user.is_authenticated())):
		return redirect("/user/login/")
	
	if(Group.objects.get(name="Author") in request.user.groups.all()):
		return writer(request)

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
	form = forms.UserForm()
	return render(request,'people/login.html',{'form':form,'category':getCategories()})

def logoutView(request):
	logout(request)
	return redirect('/')

def newUser(request):
	if(request.method == 'POST'):
		form = forms.NewForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			repeatedPassword = form.cleaned_data['repeatedPassword']
			emailAddress = form.cleaned_data['emailAddress']
			writer = form.cleaned_data['writer']
			if(not(User.objects.filter(Q(username=username)|Q(email=emailAddress)))):
				if(password == repeatedPassword):
					newUser = User.objects.create_user(username,emailAddress,password)
					newUser.save()
					if(writer):
						Group.objects.get(name="Author").user_set.add(newUser)
					
					login(request,authenticate(username=username,password=password))
					
					return redirect('/')
			else:
				return redirect('/user/new/')
		else:	
			return redirect('/user/new/')
	else:
		form = forms.NewForm()
		return render(request,"people/new.html",{'form':form,'category':getCategories()})
