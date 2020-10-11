from django.contrib import admin

from my_django_stripe.models import Item, Order, OrderItem


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Order)
