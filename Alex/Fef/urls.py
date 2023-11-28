from django.urls import path,include
from .views import *

product_patterns = [
    path('cart/', cart, name='cart'),
    path('order/', order, name='order'),
    path('product/<int:pk>', product, name='product'),
]
urlpatterns = [
    path('', main, name='main'),
    path('news/', news, name='news'),
    path('products/<int:id>/',include(product_patterns)),
    path('faq/', faq, name='faq'),
    path('game/<int:id>',index,name='game'),
    path('test/',test),
    path('set',set),
    path('get',get),
]