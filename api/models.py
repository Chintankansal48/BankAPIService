from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=11, unique=True)
    city = models.CharField(max_length=50)
