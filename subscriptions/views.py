from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import stripe

from .models import Subscription
from accounts.models import Profile

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def subscribe_page(request):
    return render(request, 'subscriptions/subscribe.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


@login_required
def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{
                'price': settings.STRIPE_SUBSCRIPTION_PRICE_ID,
                'quantity': 1,
            }],
            customer_email=request.user.email,
            success_url=request.build_absolute_uri(reverse('subscription_success')),
            cancel_url=request.build_absolute_uri(reverse('subscription_cancel')),
        )
        return redirect(checkout_session.url, code=303)

    except Exception as e:
        messages.error(request, f"Stripe error: {str(e)}")
        return redirect('subscribe')


@login_required
def subscription_success(request):
    subscription, created = Subscription.objects.get_or_create(user=request.user)
    subscription.status = 'active'
    subscription.save()

    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.is_subscriber = True
    profile.save()

    messages.success(request, 'Subscription activated successfully.')
    return render(request, 'subscriptions/success.html')


@login_required
def subscription_cancel(request):
    messages.warning(request, 'Subscription checkout was cancelled.')
    return render(request, 'subscriptions/cancel.html')
