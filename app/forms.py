from django import forms
from .models import *


class UserForm(forms.ModelForm):
       
    email = forms.EmailField(
        label = 'email',
        max_length = 1000,
        
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'email'}
        )
    )
    phone = forms.CharField(
        label = 'Phone No.',
        max_length = 1000,
        
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'phone'}
        )
    )
    location = forms.CharField(
        label = 'location',
        max_length = 1000,
        
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'location'}
        )
    )  

    
   
    
    class Meta:
        model = User
        
        fields = [ 'email','phone', 'location',
        ]

class User1Form(forms.ModelForm):
    first_name = forms.CharField(
        label = 'firstname',
        max_length = 1000,
        
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'first_name'}
        )
    )   

    last_name = forms.CharField(
        label = 'last name',
        max_length = 1000,
        
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'last_name'}
        )
    ) 
    picture=forms.FileField(
        label = 'picture',
        
        
        widget = forms.FileInput(
            attrs = {'class': 'form-control', 'name': 'picture'}
        )
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'picture',
        ]
        