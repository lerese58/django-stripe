from django.contrib import admin

from my_django_strive_test.models import Item


class AuthorAdmin(admin.ModelAdmin):
    list_display = 'Item'


admin.site.register(Item)
