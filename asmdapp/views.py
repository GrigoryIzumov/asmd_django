from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import LearningModel, Deploy, DataModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import DataModelForm


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


class ModelListView(LoginRequiredMixin, ListView):
    model = LearningModel
    template_name = 'asmdapp/index.html'
    context_object_name = 'models'
    paginate_by = 5


class UserModelListView(LoginRequiredMixin, ListView):
    model = LearningModel
    template_name = 'asmdapp/user_models.html'
    context_object_name = 'models'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return LearningModel.objects.filter(user=user).order_by('-date_created')


class ModelDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = LearningModel

    def test_func(self):
        model = self.get_object()
        if self.request.user == model.user:
            return True
        return False


class ModelCreateView(LoginRequiredMixin, CreateView):
    model = LearningModel
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LearningModel
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        model = self.get_object()
        if self.request.user == model.user:
            return True
        return False


class ModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LearningModel
    success_url = '/'

    def test_func(self):
        model = self.get_object()
        if self.request.user == model.user:
            return True
        return False


def upload(request):
    user = request.user
    if request.method == 'POST':
        file_form = DataModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')  #field name in model
        if file_form.is_valid():
            for f in files:
                file_instance = DataModel(file=f, model=LearningModel.objects.get(pk=23))
                file_instance.save()
        messages.success(request, f'Success!')
    else:
        file_form = DataModelForm()
    datamodels = DataModel.objects.filter(model=LearningModel.objects.get(pk=23))
    context = {'form': file_form, 'datamodels': datamodels}
    return render(request, 'asmdapp/upload.html', context)

