from django.db import models
from django.forms import CharField

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    alias = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True)
    update_at = models.DateField(auto_now=True, auto_now_add=False)
    USERNAME_FIELD = 'alias'

    def __str__(self) -> str:
        return self.alias