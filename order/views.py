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
        form = ItemAddOnForm(request.POST)
        if form.is_valid():
            print("VALID!")
            if(form.cleaned_data['add_on_quantity'] != 0):
                print("No quantity. Not saved.")
                newItemAddOn = form.save()
                return redirect('orderslip', order=newItemAddOn.order_item.order_id)
            return redirect('orderslip', order=form.cleaned_data['order_item'].order_id)

    form = ItemAddOnForm({'order_item':order_item})
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
    try:
        OrderSlip.objects.filter(order_id=order_id).delete()
    except:
        print("No Order Slip found.")
    LastOrderSlip = OrderSlip.objects.latest('order_id')
    return redirect('orderslip', order=LastOrderSlip.order_id)

def deleteOrderItem(request, order_item_id):
    OrderItemToDelete = OrderItem.objects.filter(order_item_id=order_item_id).first()
    try:
        OrderSlipID = OrderItemToDelete.order.order_id
        OrderItemToDelete.delete()
        return redirect('orderslip', order=OrderSlipID)
    except:
        print("No Order Item found.")
        return redirect('orderslip')
    
def deleteItemAddOn(request, item_addon_id):
    ItemAddOnToDelete = ItemAddOn.objects.filter(item_addon_id=item_addon_id).first()
    try:
        OrderSlipID = ItemAddOnToDelete.order_item.order.order_id
        ItemAddOnToDelete.delete()
        return redirect('orderslip', order=OrderSlipID)
    except:
        print("No Item Add-On found.")
        return redirect('orderslip')