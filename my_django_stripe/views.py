import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from my_django_stripe import settings
from my_django_stripe.models import Item, Order, OrderItem


def get_order_obj(order_id) -> dict:
    order = Order.objects.get(id=order_id)
    orderitems_for_order = OrderItem.objects.filter(order_id=order_id)
    orderitem_list = []
    for orderitem in orderitems_for_order:
        orderitem_obj = {'item_id': orderitem.item.id,
                         'name': orderitem.item.name,
                         'quantity': orderitem.quantity,
                         'pretotal': orderitem.quantity * orderitem.item.price}
        orderitem_list.append(orderitem_obj)
    return {'id': order.id,
            'name': order.name,
            'status': order.status,
            'total': order.total_price,
            'orderitems': orderitem_list}


def index(request):
    items = Item.objects.all().order_by('name')
    context = {'items': items}
    return render(request, 'index.html', context)


def item_page(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item.html', context)


def order_page(request, order_id):
    order = get_order_obj(order_id=order_id)
    context = {'order': order}
    return render(request, 'order.html', context)


def orders_list(request):
    orders = Order.objects.all()
    order_list = []
    for order in orders:
        order_obj = get_order_obj(order_id=order.id)
        order_list.append(order_obj)
    context = {'order_list': order_list}
    return render(request, 'orders.html', context)


@csrf_exempt
def create_checkout_session(request, order_id=None, item_id=None):
    if not order_id:
        item = Item.objects.get(id=item_id)
        order = Order.objects.create(name='UNNAMED', status='Created')
        order_item = OrderItem.objects.create(item=item, order=order, quantity=1)
        order_obj = get_order_obj(order_id=order.id)
    elif order_id:
        order_obj = get_order_obj(order_id=order_id)
    else:
        return
    domain_url = 'http://localhost:8000/'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    orderitems_list = [{'name': orderitem['name'],
                        'quantity': orderitem['quantity'],
                        'currency': 'usd',
                        'amount': int(orderitem['pretotal']) * 100} for orderitem in order_obj.get('orderitems')]
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            line_items=orderitems_list
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
