from django.contrib import admin
from users.models import StripeCustomer


admin.site.register(StripeCustomer)
# admin.site.register(Profile)