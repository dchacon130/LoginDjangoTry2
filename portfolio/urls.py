from django.urls import path
from .import views

urlpatterns = [
    path('portfolio/', views.list, name='portfolio')
]
