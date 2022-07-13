from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from order.models import OrderSlip

# Create your views here.
def index(request):
    o = OrderSlip(customer_name="Anne")
    return HttpResponse("Hello Blizzarder! You are in order.")