
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('new',views.new,name='new'),
    path('form',views.form,name='form'),
    path('submit',views.submit,name='submit'),
]
