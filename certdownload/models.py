from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name