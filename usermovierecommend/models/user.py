from django.db import models


class User(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
