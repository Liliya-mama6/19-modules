from django import forms

class User(forms.Form):
    name = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput())
    age = forms.CharField(max_length=3, label='Your age')