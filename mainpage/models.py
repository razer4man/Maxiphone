from __future__ import unicode_literals
from django.db import models
from fontawesome.fields import IconField

class Benefit(models.Model):
    icon = IconField()
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title

class Benefit_add(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title

class Connection_step(models.Model):
    step_number = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.step_number + " - "+ self.title
