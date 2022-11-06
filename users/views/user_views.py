import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # new
from django.http.response import JsonResponse, HttpResponse  # updated
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt




from users.models import StripeCustomer  

# USER SIGNUP, LOGIN, SIGNOUT
from ..forms import NewUserForm, ManageAccountForm, CancelForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Password Reset
from django.contrib.auth import views as auth_views 

# CONTACT IMPORTS
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import message 


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    
    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "You have succesfully logged out.")
    return redirect('home')

def account(request):
    return render(request, 'users/account.html')


def manage_account(request):
    form = ManageAccountForm(request.POST, instance=request.user) 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('account') # May need changed to users/account.html
        else:
            return redirect('home')
    else:
        form = ManageAccountForm(instance=request.user)
        context = {'form': form}
        return render(request, 'users/manage-account.html', context)

def cancel_subscription(request):
    form = CancelForm()
    if request.method == "POST":
        form = CancelForm(request.POST)
        if form.is_valid():
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["first_name"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, [settings.ADMIN_EMAILS])
            return redirect('home')
    context = {'form': form}
    return render(request, 'users/cancel-subscription.html', context)




