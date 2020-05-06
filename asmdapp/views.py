from django.shortcuts import render
from .models import Model, Deploy


# Create your views here.


def index(request):
    num_models = Model.objects.count()
    num_deploys = Deploy.objects.count()

    return render(
        request,
        'index.html',
        context={'num_models': num_models, 'num_deploys': num_deploys}
    )
