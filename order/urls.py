from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="order"),
    path('slip/',views.orderslip, name="orderslip"),
    path('data/', views.data, name="data")
]
