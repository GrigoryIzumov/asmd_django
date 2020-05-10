from django.urls import path
from . import views
from .views import ModelListView, ModelDetailView


urlpatterns = [
    path('', ModelListView.as_view(), name='home'),
    path('model/<int:pk>/', ModelDetailView.as_view(), name='model-detail'),
]