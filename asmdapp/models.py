from django.db import models
from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Model(models.Model):
    name = models.CharField


class Deploy(models.Model):
    name = models.CharField


class Data(models.Model):
    pass
