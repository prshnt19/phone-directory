from django.db import models

# Create your models here.

class PhoneDirectory(models.Model):
    Name = models.CharField(max_length=50, null=False)
    Number = models.IntegerField(null=False)