from django.shortcuts import render
from .models import Model, Deploy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


# @login_required
def index(request):
    num_models = Model.objects.count()
    num_deploys = Deploy.objects.count()
    context = {
        'posts': posts
    }
    return render(
        request,
        'asmdapp/index.html',
        context
    )
