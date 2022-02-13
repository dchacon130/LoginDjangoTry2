from django.contrib import admin
from .models import Portfolio

# Register your models here.
admin.site.register(Portfolio)

title = "Proyects"

admin.site.site_header = title
admin.site.site_title = title