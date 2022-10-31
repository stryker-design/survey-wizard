from ..forms import NewUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # new
from django.http.response import JsonResponse, HttpResponse  # updated
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# FREE BILLING SIGNUP

def free_billing(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful")
            return redirect('https://checkout.stripe.com/c/pay/cs_test_a1hhvBEpy5APE3jVJLg21ZwevMcY5vZlTw8wmXD6nU0tQhNe9LVN7hdr22#fidkdWxOYHwnPyd1blpxYHZxWjA0STFpcX1Nc1RTS1NsS09RV2RMcTR1PWdHPWpmZHU1PEthT39MQTRdXzAyYUZvYjdpckh0cmxzQVY9bk8wf1U1Q2pOcGsxNnUzPUNHRkFEaWlqXDZsSGNgNTU0VEk2Tmp3XCcpJ2hsYXYnP34nYnBsYSc%2FJzU8PWFmYGQ2KGA9ZzcoMTVhYSg8YTJhKD0wNzY2YTxgZDUwYTA1MGA1ZCcpJ2hwbGEnPydmPTE8ZzwzMChmNDc1KDE2MDMoZGBnZihhMjExYzQ0NmMwM2NkNjxjN2cnKSd2bGEnPyc8NDI2NWQ9YSg0PDxkKDEyPWcoPGY1MihmZmc2NTE3ZjRkPGNnMTc1Z2YneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8ndmxrYmlgWmxxYGgnKSd3YGNgd3dgd0p3bGJsayc%2FJ21xcXU%2FKippamZkaW1qdnE%2FPTU1NSd4JSUl') # Stripe redirect
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm

    context = {'form': form}
    return render(request, 'payments/billing/free-billing.html', context)

# BASIC BILLING SIGNUP

def basic_billing(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful")
            return redirect('https://checkout.stripe.com/c/pay/cs_test_a1I7a58rLk4lbiA2x8FyuTb5tpsNfYMDw00ijIFqEZ14ceUBgRHTEimqsB#fidkdWxOYHwnPyd1blpxYHZxWjA0STFpcX1Nc1RTS1NsS09RV2RMcTR1PWdHPWpmZHU1PEthT39MQTRdXzAyYUZvYjdpckh0cmxzQVY9bk8wf1U1Q2pOcGsxNnUzPUNHRkFEaWlqXDZsSGNgNTU0VEk2Tmp3XCcpJ2hsYXYnP34nYnBsYSc%2FJzU8PWFmYGQ2KGA9ZzcoMTVhYSg8YTJhKD0wNzY2YTxgZDUwYTA1MGA1ZCcpJ2hwbGEnPycwYzNnMTE0NSg0ZjIwKDFnPTYoPT01MSg9YGBkYWA8M2YyZ2cwPTM1NzwnKSd2bGEnPyc8YzdkMTRmNygyYzQzKDFhNTYoPWFjMCgxPDdkNjZhMzNjYTAzMjZgMTUneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8ndmxrYmlgWmxxYGgnKSd3YGNgd3dgd0p3bGJsayc%2FJ21xcXU%2FKippamZkaW1qdnE%2FPTU1NSd4JSUl') # Stripe redirect
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm

    context = {'form': form}
    return render(request, 'payments/billing/basic-billing.html', context)


def premium_billing(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful")
            return redirect('https://checkout.stripe.com/c/pay/cs_test_a1BIQSI9wvjq9JJb9UFedXYOcTc9kfMXyQGKvvHcUb2BGao1oMUehw6yb8#fidkdWxOYHwnPyd1blpxYHZxWjA0STFpcX1Nc1RTS1NsS09RV2RMcTR1PWdHPWpmZHU1PEthT39MQTRdXzAyYUZvYjdpckh0cmxzQVY9bk8wf1U1Q2pOcGsxNnUzPUNHRkFEaWlqXDZsSGNgNTU0VEk2Tmp3XCcpJ2hsYXYnP34nYnBsYSc%2FJzU8PWFmYGQ2KGA9ZzcoMTVhYSg8YTJhKD0wNzY2YTxgZDUwYTA1MGA1ZCcpJ2hwbGEnPyc1Mz1mNzZgPCg9YGc3KDExMDMoZ2E1MihhMDQ0Z2Q9MGZjYzFhNzJmNzQnKSd2bGEnPyc0YDVnNzE3Zyg2ZmYxKDFgY2YoPDc0MChnZGExMmMyYWE0MmdhNDUzMjcneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8ndmxrYmlgWmxxYGgnKSd3YGNgd3dgd0p3bGJsayc%2FJ21xcXU%2FKippamZkaW1qdnE%2FPTU1NSd4JSUl') # Stripe redirect
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm

    context = {'form': form}
    return render(request, 'payments/billing/premium-billing.html', context)


@login_required
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_TEST_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

# FUNCTION FOR FREE TRIAL

@csrf_exempt
def create_checkout_session_free(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID_FREE,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


# FUNCTION FOR BASIC PLAN

@csrf_exempt
def create_checkout_session_basic(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID_BASIC,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


# FUNCTION FOR PREMIUM PLAN

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})








@login_required
def cancel(request):
    context = {}
    return render(request, 'payments/cancel.html', context)

@login_required
def success(request):
    context = {}
    return render(request, 'payments/success.html', context)