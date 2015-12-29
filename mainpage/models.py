from __future__ import unicode_literals

from django.db import models


class Benefit(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title
