
from django.urls import path,include
from .import views

app_name = 'cards'
urlpatterns = [
    path('generate',views.generate,name='generate'),
    path('form',views.form,name='form'),
    path('view/<int:id>/<int:theme>',views.view,name='view'),
    
]
