from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from cards.models import Detail
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from CardGenerator import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        phone = request.POST['phone']
        password = request.POST['password']
        # if password != confirm_password:
        #     return render(request,'user/signup.html',{'message':'Password does not match'})
        if User.objects.filter(username = username).exists():
             return render(request,'user/signin.html',{'message':'User already exists with that username Please sign in'})
        user = User.objects.create_user(username = username, password = password,name=name,phone=phone)
        user.is_active = False
        user.email = username
        token = default_token_generator.make_token(user)

        # Build verification URL
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        verification_url = request.build_absolute_uri('/userverify_email/{}/{}/'.format(uid, token))
        subject =  ''' Welcome to Card Generator, Verify your account'''
        message =  '''
        Hello {},
                Welcome to Card Generator, the ultimate platform for designing business cards! We're thrilled to have you on board as a new user. With our easy-to-use interface and powerful design tools, you'll be able to create stunning business cards.

                Get started by logging into your account and exploring the wide range of customizable templates we offer. Whether you're looking for a sleek and professional design or something more creative and unique, we have options to suit every style.

                Customize your business card with your logo, contact information, and a brief description of your services or expertise. Our intuitive editor allows you to adjust fonts, colors, and layouts, ensuring your business card perfectly represents your brand.

                Once you're satisfied with your design, simply save it and share high-quality printed cards right from our site. 

                If you have any questions or need assistance along the way, our friendly support team is here to help. Enjoy your journey with Card Generator, and we can't wait to see the fantastic business cards you create
                Please click on the link below to verify your email address and complete the registration of your account:\n\n{}\n\nThank you for using our site!\n\nCard Generator Team'''.format(user.name, verification_url)
        email_from = settings.EMAIL_HOST_USER
        # send_mail(subject, message, email_from, [username,])


        # Prepare email message
        # subject = 'Welcome to Card Generator'
        # message = "Hi {},\n\nWelcome to Card Generator! Please click on the link below to verify your email address and complete the registration of your account:\n\n{}\n\nThank you for using our site!\n\nCard Generator Team".format(user.username, verification_url)
        # email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [username, ])
        user.save()
        return render(request, 'user/signin.html', {'message': 'User created successfully. Please check your email for verification instructions.'})
    
        
        
    return render(request,'user/signup.html')

def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'user/verification_success.html')
        else:
            return render(request, 'user/verification_failure.html')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request, 'user/verification_failure.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists
        if not User.objects.filter(username=username).exists():
            return render(request, 'user/signup.html', {'message': "User doesn't exist. Please sign up"})
        
        user = User.objects.get(username=username)
        
        # Check if the user account is verified
        if not user.is_active:
            return render(request, 'user/signin.html', {'message': 'User account is not verified yet. Please check your email for verification instructions.'})
        
        # Authenticate the user with credentials
        authenticated_user = authenticate(username=username, password=password)
        
        if authenticated_user is not None:
            if authenticated_user.is_active:
                request.session['username'] = username
                login(request, authenticated_user)
                return redirect('/')
        
        return render(request, 'user/signin.html', {'message': 'Incorrect username or password'})
    
    return render(request, 'user/signin.html')

def logout_view(request):
    
    del request.session['username']
    logout(request)
    return render(request,'user/signin.html',{'message':'Logged out successfully'})


from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

class CustomPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'
    success_url = reverse_lazy('user:password_reset_done')  # Update the URL name
    email_template_name = 'user/reset_password.html'
    extra_email_context = {'protocol': 'http', 'domain': '127.0.0.1:8000'}
    
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse_lazy

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')
    form_class = SetPasswordForm