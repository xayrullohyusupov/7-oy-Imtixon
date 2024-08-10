from django.shortcuts import render, redirect, get_object_or_404
from .models import Xodim, Davomat
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login



def index(request):
    xodimlar = Xodim.objects.all()
    xodimlar_davomat = []
    for xodim in xodimlar:
        oxirgi_davomat = Davomat.objects.filter(xodim=xodim).order_by('-kelgan_vaqti').first()
        xodimlar_davomat.append({
            'xodim': xodim,
            'davomat': oxirgi_davomat
        })
    return render(request, 'index.html', {'xodimlar_davomat': xodimlar_davomat})

def create_employee(request):
    if request.method == 'POST':
        xodim = Xodim(
            ism=request.POST.get('ism'),
            familiya=request.POST.get('familiya'),
            email=request.POST.get('email'),
            lavozim=request.POST.get('lavozim')
        )
        xodim.save()
        return redirect('index')
    return render(request, 'create_employee.html')


def update_employee(request, id):
    xodim = get_object_or_404(Xodim, id=id)
    if request.method == 'POST':
        xodim.ism = request.POST.get('ism')
        xodim.familiya = request.POST.get('familiya')
        xodim.email = request.POST.get('email')
        xodim.lavozim = request.POST.get('lavozim')
        xodim.save()
        return redirect('index')
    return render(request, 'update_employee.html', {'xodim': xodim})


def delete_employee(request, id):
    xodim = get_object_or_404(Xodim, id=id)
    if request.method == 'POST':
        xodim.delete()
        return redirect('index')
    return render(request, 'delete_employee.html', {'xodim': xodim})

def mark_attendance(request, id):
    xodim = get_object_or_404(Xodim, id=id)
    Davomat.objects.create(xodim=xodim, kelgan_vaqti=timezone.now())
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
