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

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.user)