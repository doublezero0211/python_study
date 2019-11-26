from django.contrib import admin
from pizzas.models import Pizza
from pizzas.models import Topping

admin.site.register(Pizza)
admin.site.register(Topping)
