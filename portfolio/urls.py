from django.urls import path
from .import views

urlpatterns = [
    path('portfolio/', views.list, name='portfolio'),
    path('save-portfolio', views.save_porfolio, name="save"),
    path('delete-portfolio/<int:id>', views.delete_portfolio, name="delete-portfolio")
]
