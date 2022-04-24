from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class registermodel(User):
    dor=models.DateTimeField(default=timezone.now)


class exam_model(models.Model):
    questions = models.CharField(max_length=200)


class Contact_Model(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    phone = models.BigIntegerField()
    desc = models.CharField(max_length=4141)

    def __str__(self):
        return self.username