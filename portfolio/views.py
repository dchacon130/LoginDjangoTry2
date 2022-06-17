from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Portfolio, Knowledge
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="login")
def list(request):
    all_portfolio = Portfolio.objects.all()
    knowledge_lvl = Knowledge.objects.all()
    know = Portfolio.objects.select_related().filter(pk=1)

    return render(request, 'portfolio/portfolio.html', {
        'title': 'Portfolio',
        'portfolios': all_portfolio,
        'knowledges': knowledge_lvl,
        'know': know
    })

def save_porfolio(request):

    if request.method == 'POST':
        
        title = request.POST['title']
        experience = request.POST['years']
        knowledge = request.POST['knowledge']
        description = request.POST['description']

        registro = Portfolio(
            title = title,
            description = description,
            experience = experience,
            knowledge_id = knowledge
        )
        registro.save()
        
        messages.success(request, f'Record created successfully!')
        return redirect('portfolio')
    else:
        messages.error(request, f'Record not created')
        return redirect('portfolio')

def delete_portfolio(request, id):
    

    return redirect('portfolio')