from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    
    print(Award.objects.filter(user=request.user).aggregate(points=Sum('points')))
    return render(request,'app/profile.html',{
        'form':UserForm(),
        'form1':User1Form(),
        'data':request.user,
        'awards':Award.objects.filter(user=request.user),
        'points':Award.objects.filter(user=request.user).aggregate(points=Sum('points')),
    })

@login_required
def update(request):
    instance = get_object_or_404(User,pk=request.user.id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST or None, instance = instance)
        print('eee',request.POST)
      
        
        
        # check whether it's valid:
        if form.is_valid():
            
            form.save()
            
            return HttpResponseRedirect(reverse('index'))

    

    return HttpResponseRedirect(reverse('index'))


def update1(request):
    instance = get_object_or_404(User,pk=request.user.id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = User1Form(request.POST, request.FILES or None, instance = instance)
        print('eee',request.FILES)
      
        
        
        # check whether it's valid:
        if form.is_valid():
           
            
            form.save()
          
            return HttpResponseRedirect(reverse('index'))

    

    return HttpResponseRedirect(reverse('index'))
