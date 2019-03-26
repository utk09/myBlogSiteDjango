from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def index(request):
    # return HttpResponse('Hello from my new Posts!')

    posts = Posts.objects.all()[:10]
    data = {
        'title': 'My Posts',
        'posts': posts

    }

    return render(request, 'posts/index.html', data)

def details(request, id):
    post = Posts.objects.get(id = id)

    data = {
        'post':post
    }
    return render(request, 'posts/details.html', data)

