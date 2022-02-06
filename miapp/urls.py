from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('inicio/', views.index_page, name='index'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('about/', views.about_page, name='about'),
    path('email/', views.email_page, name='email'),
]