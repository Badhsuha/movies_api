from django.db import models
import json

class Movies(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    updateAt = models.DateTimeField()
    def __str__(self):
        return self.title

