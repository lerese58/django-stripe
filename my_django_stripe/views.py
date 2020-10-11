import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from my_django_stripe import settings
from my_django_stripe.models import Item


def index(request):
    items = Item.objects.all().order_by('name')
    context = {'items': items}
    return render(request, 'index.html', context)


def item_page(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item.html', context)


@csrf_exempt
def create_checkout_session(request, item_id):
    item = Item.objects.get(id=item_id)
    domain_url = 'http://localhost:8000/'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'name': item.name,
                    'quantity': 1,
                    'currency': 'usd',
                    'amount': int(item.price * 100),
                }
            ]
        )
        return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
        return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_config(request):
    stripe_conf = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_conf, safe=False)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
