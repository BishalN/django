from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

def hello(request):
    return HttpResponse('<h3>hello how si</h3>',{'title':'about'})

# Create your views here.
