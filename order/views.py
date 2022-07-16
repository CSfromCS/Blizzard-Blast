from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from order.models import *

# Create your views here.
def index(request):
    o = OrderSlip(customer_name="Anne")
    return HttpResponse("Hello Blizzarder! You are in order.")

def orderslip(request):
    context = {
        'Recipe' : Recipe.objects.all(),
        'Ingredient' : Ingredient.objects.all(),
        'OrderSlip' : OrderSlip.objects.all(),
        'OrderItem' : OrderItem.objects.all(),
        'ItemAddOn' : ItemAddOn.objects.all()
    }
    return render(request, 'orderslip.html', context=context)

def data(request):
    context = {
        'Recipe' : Recipe.objects.all(),
        'Ingredient' : Ingredient.objects.all(),
        'OrderSlip' : OrderSlip.objects.all(),
        'OrderItem' : OrderItem.objects.all(),
        'ItemAddOn' : ItemAddOn.objects.all()
    }
    return render(request, 'data.html', context=context)