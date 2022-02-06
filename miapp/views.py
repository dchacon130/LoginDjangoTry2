from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index_page(request):

    return render(request, 'miapp/index.html', {
        'title': 'Soy index'
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
            'title': 'Soy registro',
            'register_form': register_form
        })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/inicio')
        else:
            messages.warning(request, 'Por favor verifique el usuario y contraseña!')

    return render(request, 'users/login.html', {
        'title': 'Soy login'
    })


def logout_page(request):
    logout(request)
    return redirect('login')

def about_page(request):

    return render(request, 'miapp/about.html', {
        'title': 'Soy about'
    })

def email_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        send_mail(
            'Correo enviado desde Django',
            mensaje,
            settings.EMAIL_HOST_USER, 
            [email],
            fail_silently=False
        )
        return redirect('/inicio')

    return render(request, 'miapp/email.html', {
        'title': 'Soy Email'
    })
    