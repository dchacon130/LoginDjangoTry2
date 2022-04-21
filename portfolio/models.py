from django.db import models
# Create your models here.

class Knowledge(models.Model):
    title = models.CharField(max_length=2)
    description = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Knowledge'
        
    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    experience = models.IntegerField(default=0)
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE,null=True, blank=True)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Portfolio'
        
    def __str__(self):
        return self.title, self.description, self.create_at
