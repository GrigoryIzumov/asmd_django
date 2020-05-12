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


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return f'{instance.model.user.username}/{filename}'


class DataModel(models.Model):
    model = models.ForeignKey(LearningModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)

