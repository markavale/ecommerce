from django.urls import path
from . views import  (ItemDetailView, IndexView, add_to_cart,
     remove_from_cart, OrderSummaryView, CheckOutView,
     remove_single_item_from_cart, PaymentView, AddCouponView,
     RequestRefundView

)


app_name= 'core'

urlpatterns = [
    path('',  IndexView.as_view(), name='item-list'),
    path('checkout/',  CheckOutView.as_view(), name='checkout'),
    path('payment/<payment_option>/',  PaymentView.as_view(), name='payment'),
    path('product/<slug>/',  ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

]