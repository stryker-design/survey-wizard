from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.shortcuts import redirect


# DRF IMPORTS
from rest_framework.response import Response
from rest_framework.decorators import api_view

# CONTACT IMPORTS
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import message 




def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def roadmap(request):
    context = {}
    return render(request, 'core/roadmap.html', context)

def privacy(request):
    context = {}
    return render(request, 'core/privacy.html', context)

def terms_conditions(request):
    context = {}
    return render(request, 'core/terms-conditions.html', context)

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["first_name"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, [settings.ADMIN_EMAILS])
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/contact.html', context)

def not_found(request, exception):
    return render('request', 'core/not-found.html')



