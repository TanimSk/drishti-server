from django.db import models


class PreOrder(models.Model):
    product = models.CharField(max_length=500)
    quantity = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField()
    address = models.TextField()
    comment = models.TextField()
