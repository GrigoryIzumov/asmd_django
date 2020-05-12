from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class LearningModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('model-detail', kwargs={'pk': self.pk})


class Deploy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


