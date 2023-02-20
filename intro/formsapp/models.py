from django.db import models


class Message(models.Model):
    CHOICES = (
        ('q', 'Pytanie'),
        ('o', 'Inne'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=10, choices=CHOICES)
    title = models.CharField(max_length=100)
    body = models.TextField()

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
