import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(user_email, plan_id):
    return stripe.checkout.Session.create(
        mode="subscription",
        customer_email=user_email,
        line_items=[{
            "price": plan_id,
            "quantity": 1
        }],
        success_url="https://app.seusaas.com/success",
        cancel_url="https://app.seusaas.com/billing"
    )