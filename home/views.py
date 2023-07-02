from django.shortcuts import render
from cards.models import Detail
from user.models import User
# Create your views here.

def home(request):
    if request.session.get('username'):
        cards = Detail.objects.filter(created_for=User.objects.get(username=request.session['username']))
        return render(request,'home/index.html',{
            'cards':cards
        } )
    return render(request, 'home/index.html')


def contact(request):
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
