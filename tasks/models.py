from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import DateField
from traitlets import default

# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text