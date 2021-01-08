from django.http import HttpResponse
from django.shortcuts import render


posts = [
    {
        'author':"bishal neupane",
        'title':"the best and fastest typer in history of human kind",
        'content':"this is the fake information about bishal the great person of the world",
        'date_posted':"august 2nd"
    }, 
    {
        'author':'john doe',
        'title':'the faku of the faker in the universe of the great people',
        'content':'this is very beautiful day how is the world out there ',
        "date_posted":"2nd May"
    }
]

def home(request):
    context = {
        'posts':posts,
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

def hello(request):
    return HttpResponse('<h3>hello how si</h3>',{'title':'about'})

# Create your views here.
