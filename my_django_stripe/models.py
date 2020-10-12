from django.db import models


class TotalPriceManager(models.Manager):
    def get_query_set(self):
        return super(TotalPriceManager, self).get_query_set(Item.price * OrderItem.quantity)


class Item(models.Model):
    name = models.CharField(max_length=127, null=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    # orders = models.ManyToManyField('Order', through='OrderItem')
    # currency = models.CharField(choices=[])


class OrderItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    name = models.CharField(max_length=20, default='ORDER_UNNAMED')
    orderitems = models.ManyToManyField('Item', through='OrderItem')
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Created')

    @property
    def total_price(self):
        total = 0
        orderitems = OrderItem.objects.filter(order=self)
        for orderitem in orderitems:
            total += orderitem.quantity * orderitem.item.price
        return total

# class Discount(models.Model):
#     order = models.ForeignKey(to=Order, null=True, blank=True)
#     amount = models.DecimalField(decimal_places=2)
#
#
# class Tax(models.Model):
#     order = models.ForeignKey(to=Order)
#     amount = models.DecimalField(decimal_places=2)
