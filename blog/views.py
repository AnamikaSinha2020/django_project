from django.shortcuts import render
from django.http import  HttpResponse

posts=[
    {
        'author':'Anamika',
        'title':'Blog post',
        'content': 'First Post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'jane Doe',
        'title':'Blog post 2',
        'content': 'Second Post content',
        'date_posted':'August 28, 2018'
    }
]


# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})





