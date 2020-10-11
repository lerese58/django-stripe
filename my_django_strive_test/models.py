from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    # currency = models.CharField(choices=[])

#
# class Order(models.Model):
#     # todo: ArrayField fr postgresql
#     items = models.JSONField()
#     total_price = models.DecimalField(decimal_places=2)
#
#
# class Discount(models.Model):
#     order = models.ForeignKey(to=Order, null=True, blank=True)
#     amount = models.DecimalField(decimal_places=2)
#
#
# class Tax(models.Model):
#     order = models.ForeignKey(to=Order)
#     amount = models.DecimalField(decimal_places=2)
