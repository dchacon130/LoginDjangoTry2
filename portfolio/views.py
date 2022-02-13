from turtle import title
from django.shortcuts import render
from .models import Portfolio
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def list(request):
    all_portfolio = Portfolio.objects.all()

    return render(request, 'portfolio/list.html', {
        'title': 'Portfolio',
        'portfolios': all_portfolio
    })
