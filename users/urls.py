from django.contrib import admin
from django.urls import path, include
from .views import user_views, payment_views

# PASSWORD RESET
from django.contrib.auth import views as auth_views 




# Import Classes



urlpatterns = [

        # USER REGISTRATION, LOGIN, LOGOUT
        path('signup/', user_views.signup, name='signup'),
        path('login/', user_views.login_request, name='login'),
        path('logout/', user_views.logout_request, name='logout'),
        path('account/', user_views.account, name='account'),
        path('manage-account/', user_views.manage_account, name='manage-account'),
        path('cancel-subscription/', user_views.cancel_subscription, name='cancel-subscription'),

        # PASSWORD RESET
        # Submit email form
        path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password-reset/reset_password.html'), name='reset_password'),

        # Email sent success message
        path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset/reset_password_done.html'), name='password_reset_done'),

        # Link to password reset from in email
        path('reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset/reset_password_confirm.html'), name='password_reset_confirm'),

        # Password succesfully changed
        path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset/reset_password_complete.html'), name='password_reset_complete'),


        # STRIPE PAYMENTS
        path('config/', payment_views.stripe_config, name='stripe'),
        path('create-checkout-session-free/', payment_views.create_checkout_session_free), 
        path('create-checkout-session-basic/', payment_views.create_checkout_session_basic), 
        path('create-checkout-session/', payment_views.create_checkout_session), 
     

        # PAYMENT REDIRECTS
        path('free-billing/', payment_views.free_billing, name='free-billing'),
        path('basic-billing/', payment_views.basic_billing, name='basic-billing'),
        path('premium-billing/', payment_views.premium_billing, name='premium-billing'),
        path('cancel/', payment_views.cancel, name='cancel'),
        path('success/', payment_views.success, name='success'),


        #  AUTHENTICATION
        path('accounts/', include('allauth.urls')),
        
]