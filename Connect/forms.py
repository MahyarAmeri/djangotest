from django import forms
from django.contrib.auth.models import User
user = User.objects.all()
class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
class massageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    receiver = forms.ModelChoiceField(queryset=user , widget=forms.Select(attrs={'class':'form-control'}))