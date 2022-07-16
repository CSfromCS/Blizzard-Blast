from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from order.models import *

# Create your views here.
def index(request):
    o = OrderSlip(customer_name="Anne")
    return HttpResponse("Hello Blizzarder! You are in order.")

def orderslip(request):
    NewOrderSlip = OrderSlip(customer_name="Anne")
    context = {
        'Recipe' : Recipe.objects.all(),
        'Ingredient' : Ingredient.objects.all(),
        'NewOrderSlip' : NewOrderSlip,
        'OrderSlip' : OrderSlip.objects.all(),
        'OrderItem' : OrderItem.objects.all(),
        'ItemAddOn' : ItemAddOn.objects.all()
    }
    return render(request, 'orderslip.html', context=context)