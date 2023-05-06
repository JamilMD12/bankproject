from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView
from bankapp.models import MyForm


# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
    return render(request, "register.html")
def new(request):
    return render(request,"new.html")
def form(request):

    return render(request,"form.html")
def submit(request):

    return render(request,"submit.html")
# def new(request):
#     return render(request,"form.html")
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
# # def my_form(request):
# #     if request.method=="POST":
# #         form=MyForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #         else:
# #             form=MyForm()
# #         return render(request,'form.html',{'form':form})
#
def add_form(request):
    task1 = MyForm.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        dob=request.POST.get('dob','')
        age=request.POST.get('age','')
        gender = request.POST.get('gender', '')
        phoneno = request.POST.get('phoneno', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        task=MyForm(name=name, dob=dob,age=age,gender=gender,phoneno=phoneno,email=email,address=address,district=district,branch=branch)
        task.save()
    return render(request,'home.html',{'task':task1})
#
#
# class Tasklistview(ListView):
#     model=MyForm
#     template_name = 'home.html'
#     context_object_name = 'task'