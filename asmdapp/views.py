from django.shortcuts import render
from .models import LearningModel, Deploy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


# Create your views here.

@login_required
def index(request):

    context = {
        'models': LearningModel.objects.filter(user=request.user)
    }
    return render(
        request,
        'asmdapp/index.html',
        context
    )


class ModelListView(ListView):
    model = LearningModel
    template_name = 'asmdapp/index.html'
    context_object_name = 'models'
    ordering = ['-date_created']


class ModelDetailView(DetailView):
    model = LearningModel
