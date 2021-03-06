from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail

#Reset Password 
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Create your views here.
def index_page(request):

    return render(request, 'miapp/index.html', {
        'title': 'Index'
    })

def register_page(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Se ha registrado correctamente!')
                return redirect('index')

        return render(request, 'users/register.html', {
            'title': 'Register',
            'register_form': register_form
        })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            messages.warning(request, 'No pudeste loguear jajaja')

    return render(request, 'users/login.html', {
        'title': 'Login',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    })


def logout_page(request):
    logout(request)
    return redirect('login')

def about_page(request):

    return render(request, 'miapp/about.html', {
        'title': 'About'
    })

def email_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        mesasge = request.POST.get('mensaje')
        subject = 'Correo enviado desde Django'

        send_mail(
            subject,
            mesasge,
            settings.EMAIL_HOST_USER, 
            [email],
            fail_silently=False
        )
        return redirect('/index')

    return render(request, 'miapp/email.html', {
        'title': 'Email'
    })


    
#Reset Password
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})