
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),    
    path('cards', include('cards.urls', namespace='cards')),
    path('user', include('user.urls', namespace='user')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('previous',views.previous,name='previous'),
]
