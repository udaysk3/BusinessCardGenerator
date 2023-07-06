from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from user.models import User
from django.urls import reverse
from . models import Detail
from django.contrib import messages
from bs4 import BeautifulSoup
# Create your views here.

def generateForm(request):
    if request.session.get('username') and request.method == 'POST' :
        name = request.POST['name']
        profileimage = request.FILES['profileimage']
        email = request.POST['email']
        role = request.POST['role']
        phone = request.POST['phone']
        companyname = request.POST['companyname']
        companylogo = request.FILES['logo']
        website = request.POST['website']   
        address = request.POST['address']
        created_for = User.objects.get(username=request.session['username'])
        details = Detail(name=name,email=email,role=role,phone=phone,profileimage = profileimage,companyname=companyname,companylogo=companylogo,website=website,address=address,created_for=created_for)
        details.save()
        print(details.id)
            # return view(request=request,id=details.id,theme=1)
        messages.success(request,'Card Generated Successfully')
        
        return render(request,'cards/generate.html',{'message' : "Card Generated Successfully",'details':details,'username':name,'id':details.id,})
    else:
        return render(request,'user/signin.html',{'message' : "You need to sigin to generate Cards"})
    
    
def generate(request,id):
    if request.session.get('username') and request.method == 'GET':
        details = Detail.objects.get(id = id)
        messages.success(request,'Card Generated Successfully')
        return render(request,'cards/generate.html',{'message' : "Card Generated Successfully",'details':details,'username':details.name,'id':details.id,})


def form(req):
    if req.session.get('username',None)==None:
        return render(req,'user/signin.html',{'message' : "You need to sigin to generate Cards"})
    return render(req,'cards/form.html')


def view(req,id,theme):
    details = Detail.objects.get(id=id)
    username = details.name
    user = User.objects.get(username=req.session['username'])
    print(user)
    if theme >2 and theme <10:
        if user.paid_member==True:
            return render(req,'cards/card'+str(theme)+'.html',{'username':username,'details':details,'id':id,'theme':theme})
        else:
            messages.error(req,'You need to be a paid member to use this theme')
            return redirect('payment:process_payment')
    return render(req,'cards/card'+str(theme)+'.html',{'username':username,'details':details,'id':id,'theme':theme})

