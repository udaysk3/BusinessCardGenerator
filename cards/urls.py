
from django.urls import path,include
from .import views

app_name = 'cards'
urlpatterns = [
    path('generateForm',views.generateForm,name='generateForm'),
    path('generate/<int:id>',views.generate,name='generate'),
    path('closead/<int:id>/<int:theme>',views.closead,name='closead'),
    path('form',views.form,name='form'),
    path('download/<int:id>/<int:theme>',views.download,name='download'),
    path('view/<int:id>/<int:theme>',views.view,name='view'),
    
]
