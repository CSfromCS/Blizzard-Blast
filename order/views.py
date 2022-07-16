from hashlib import new
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from .forms import *

from order.models import *

# Create your views here.
def index(request):
    o = OrderSlip(customer_name="Anne")
    return HttpResponse("Hello Blizzarder! You are in order.")

def orderslip(request, order=OrderSlip.objects.latest('order_id').order_id):
    print(order)
    context = {
        'LastOrderSlip' : OrderSlip.objects.filter(order_id=order).first(),
        'OrderItem' : OrderItem.objects.filter(order=order),
        'ItemAddOn' : ItemAddOn.objects.all(),
        'OrderSlip' : OrderSlip.objects.all()
    }
    return render(request, 'orderslip.html', context)

def neworderslip(request):
    if request.method == 'POST':
        form = OrderSlipForm(request.POST)
        if form.is_valid():
            print("VALID!")
            customer_name = form.cleaned_data['customer_name']
            date_ordered = form.cleaned_data['date_ordered']

            print(customer_name, date_ordered)
            newOrderSlip = form.save()
            return redirect('orderslip', order=newOrderSlip.order_id)

    form = OrderSlipForm()
    return render(request, 'form.html', {'form' : form})

def neworderitem(request, order):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            print("VALID!")
            newOrderItem = form.save()
            return redirect('orderslip', order=newOrderItem.order_id)

    form = OrderItemForm({'order':order})
    return render(request, 'form.html', {'form' : form})

def newitemaddon(request, order_item):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            print("VALID!")
            form.save()
            return redirect('orderslip')

    form = OrderItemForm({'order_item':order_item})
    return render(request, 'form.html', {'form' : form})

def data(request):
    context = {
        'Recipe' : Recipe.objects.all(),
        'Ingredient' : Ingredient.objects.all(),
        'OrderSlip' : OrderSlip.objects.all(),
        'OrderItem' : OrderItem.objects.all(),
        'ItemAddOn' : ItemAddOn.objects.all()
    }
    return render(request, 'data.html', context=context)

def deleteOrderSlip(request, order_id):
    OrderSlip.objects.filter(order_id=order_id).delete()
    LastOrderSlip = OrderSlip.objects.latest('order_id')
    return redirect('orderslip', order=LastOrderSlip.order_id)