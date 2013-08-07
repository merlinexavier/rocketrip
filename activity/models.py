from django.db import models
from django.forms import ModelForm


class Activity(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    date = models.DateField()
    description = models.TextField(max_length=150)


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
