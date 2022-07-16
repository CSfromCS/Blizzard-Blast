from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="order"),
    path('slip/',views.orderslip, name="orderslip"),
    path('slip/<int:order>',views.orderslip, name="orderslip"),
    path('slip/new/',views.neworderslip, name="neworderslip"),
    path('item/new/<int:order>/',views.neworderitem, name="neworderitem"),
    path('item/addon/new/<int:order_item>',views.newitemaddon, name="newitemaddon"),
    path('data/', views.data, name="data"),
    path('delete/<int:order_id>', views.deleteOrderSlip, name="deleteOrderSlip")
]
