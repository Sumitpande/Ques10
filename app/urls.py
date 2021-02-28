
from django.urls import path,include
from . import views 
from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    path('',login_required(views.index),name='index'),
    path('update/',views.update,name='update'),
    path('update1/',views.update1,name='update1'),
    
]
