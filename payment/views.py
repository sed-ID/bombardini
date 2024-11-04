# payment/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Payment
import stripe
from django.conf import settings
import json

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def payment(request):
    if request.method == 'GET':
        return render(request, 'payment/payment.html', {'STRIPE_TEST_PUBLIC_KEY': settings.STRIPE_TEST_PUBLIC_KEY})

    if request.method == 'POST':
        data = json.loads(request.body)
        payment_method_id = data.get('payment_method_id')
        card_number = data.get('card_number')  # Assume these are sent from the frontend
        ssn_number = data.get('ssn_number')    # Security consideration here
        expiry_date = data.get('expiry_date')  # e.g., '2023-12-31'
        amount = data.get('amount')             

        try:
            # Create a PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(float(amount) * 100),  # Convert to cents
                currency='usd',
                payment_method=payment_method_id,
                confirmation_method='manual',
                confirm=True,
            )
            # Save payment details to the database
            Payment.objects.create(
                user=request.user,
                card_number=card_number,
                ssn_number=ssn_number,
                expiry_date=expiry_date,
                amount=amount
            )
            return redirect('payment:thank_you')  # Redirect to Thank You page
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

def thank_you(request):
    return render(request, 'payment/thank_you.html')
