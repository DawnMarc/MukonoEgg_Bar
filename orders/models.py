from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Order (models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    delivery_date = models.DateField(blank=True, default=timezone.now())
    product_id = models.TextField(max_length=300, default='egg-510')
    payment_option = models.CharField(max_length=50)
    px_per_tray = models.IntegerField(default=9000)
    px_per_egg = models.IntegerField(default=300)
    no_of_trays = models.IntegerField(null=False, default=0)
    amount = models.IntegerField()
    order_status = models.CharField(max_length=50)


class Collected(models.Model):
    eggs = models.IntegerField()
    trays = models.CharField(max_length=50)
    damaged = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)