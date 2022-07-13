from django.contrib import admin

# Register your models here.
# from order.models import OrderSlip, Recipe, OrderItem, Ingredient, ItemAddOn

from django.apps import apps
admin.site.register(apps.all_models['order'].values())


## If want to add all apps including background ones.
# from django.apps import apps
# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass