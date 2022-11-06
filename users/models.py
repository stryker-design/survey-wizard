from django.contrib.auth.models import User
from django.db import models
from django.contrib.sites.models import Site


class Sites(models.Model):
    sites = models.ManyToManyField(Site)

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class CancelSubscription(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email