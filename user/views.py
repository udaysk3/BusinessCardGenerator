from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from cards.models import Detail
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from CardGenerator import settings
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request,'user/signup.html',{'message':'Password does not match'})
        if User.objects.filter(username = username).exists():
             return render(request,'user/signup.html',{'message':'User already exists with that username Please sign in'})
        user = User.objects.create_user(username = username, password = password)
        subject =  ''' Welcome to Card Generator'''
        message =  '''
Welcome to Card Generator, the ultimate platform for designing business cards! We're thrilled to have you on board as a new user. With our easy-to-use interface and powerful design tools, you'll be able to create stunning business cards.

Get started by logging into your account and exploring the wide range of customizable templates we offer. Whether you're looking for a sleek and professional design or something more creative and unique, we have options to suit every style.

Customize your business card with your logo, contact information, and a brief description of your services or expertise. Our intuitive editor allows you to adjust fonts, colors, and layouts, ensuring your business card perfectly represents your brand.

Once you're satisfied with your design, simply save it and share high-quality printed cards right from our site. 

If you have any questions or need assistance along the way, our friendly support team is here to help. Enjoy your journey with Card Generator, and we can't wait to see the fantastic business cards you create'''
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [username,])
        user.save()
        
        return render(request,'user/signup.html',{'message':'User created successfully, Now you can sign in'})
    return render(request,'user/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username = username).exists():
             return render(request,'user/signin.html',{'message':"User doesn't exist Please sign up"})
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return render(request,'home/index.html')
        return render(request,'user/signin.html',{'message':'Incorrect Username or Password'})
    return render(request,'user/signin.html')

def logout(request):
    del request.session['username']
    return render(request,'user/signin.html',{'message':'Logged out successfully'})