from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="order"),
    path('slip/',views.orderslip, name="orderslip"),
    path('slip/<int:order>',views.orderslip, name="orderslip"),
    path('slip/new/',views.neworderslip, name="neworderslip"),
    path('slip/delete/<int:order_id>', views.deleteOrderSlip, name="deleteOrderSlip"),

    path('item/new/<int:order>/',views.neworderitem, name="neworderitem"),
    path('item/delete/<int:order_item_id>', views.deleteOrderItem, name="deleteOrderItem"),
    
    path('item/addon/new/<int:order_item>',views.newitemaddon, name="newitemaddon"),
    path('item/addon/delete/<int:item_addon_id>', views.deleteItemAddOn, name="deleteItemAddOn"),

    path('data/', views.data, name="data"),
]
