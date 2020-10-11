"""my_django_stripe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_django_stripe import views

urlpatterns = [
    path('', views.index),
    path('item/<int:item_id>', views.item_page),
    path('order/<int:order_id>', views.order_page),
    path('order/<int:order_id>/buy', views.create_checkout_session),
    path('buy/<int:item_id>', views.create_checkout_session),
    path('orders/', views.orders_list),
    path('config/', views.stripe_config),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('admin/', admin.site.urls),
]
