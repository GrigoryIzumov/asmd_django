from django.urls import path
from . import views
from .views import (ModelListView,
                    ModelDetailView,
                    ModelCreateView,
                    ModelUpdateView,
                    ModelDeleteView,
                    UserModelListView)


urlpatterns = [

    path('', ModelListView.as_view(), name='home'),
    path('user/<str:username>/', UserModelListView.as_view(), name='user-models'),
    path('model/<int:pk>/', ModelDetailView.as_view(), name='model-detail'),
    path('model/new/', ModelCreateView.as_view(), name='model-create'),
    path('model/<int:pk>/update/', ModelUpdateView.as_view(), name='model-update'),
    path('model/<int:pk>/delete/', ModelDeleteView.as_view(), name='model-delete'),
]
