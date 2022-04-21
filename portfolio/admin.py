from django.contrib import admin
from .models import Portfolio, Knowledge

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Knowledge)

titleProyects = "Proyects"

admin.site.site_header = titleProyects
admin.site.site_title = titleProyects