from django import forms

class UserForm(forms.Form):
	username = forms.CharField(label="Username",max_length=30)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

class NewForm(forms.Form):
	username = forms.CharField(label="Username",max_length=30)
	password = forms.CharField(label="Password",widget=forms.PasswordInput)
	repeatedPassword = forms.CharField(label="Repeat Password",widget=forms.PasswordInput)
	emailAddress = forms.CharField(label="Email Address",widget=forms.EmailInput)
	writer = forms.BooleanField(label="Writer")
