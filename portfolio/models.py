from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    experience = models.IntegerField(default=0)
    create_at = models.DateField(auto_now=False, auto_now_add=True)
    update_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Portfolio'
        
    def __str__(self):
        return self.title
