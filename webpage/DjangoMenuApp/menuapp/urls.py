from django.urls import path
from .views import register_view, login_view, logout_view, menu_list, add_menu_item, cart_view, add_to_cart, checkout_view,checkout_complete_view
from .views import cart_view, remove_from_cart
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('menus/', menu_list, name='view_menus'),
    path('menus/add/', add_menu_item, name='add_menu'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('cart/remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/complete/', checkout_complete_view, name='checkout_complete'), 
]
