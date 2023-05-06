from django.contrib import admin

# Register your models here.
from .models import MyForm
admin.site.register(MyForm)