from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout

from general.models import CustomUser
from .forms import CustomUserForm
from .email_backend import EmailBackend
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {
        'title' : 'Nova - Homepage',
        'class' : 'class="active"'
    }
    return render(request, 'general/index.html', context)

def about(request):
    context = {
        'title' : 'Nova - About',
        'sub_title' : 'About',
        
    }
    return render(request, 'general/about.html', context)

def services(request):
    context ={
        'title' : 'Nova - Services',
        'sub_title' : 'Services',
       
    }
    return render(request, 'general/services.html', context)

def portfolio(request):
    context= {
        'title' : 'Nova - Portfolio',
        'sub_title' : 'Portfolio',
      
    }
    return render(request, 'general/portfolio.html', context)

def team(request):
    context = {
        'title' : 'Nova - Team',
        'sub_title' : 'Team',
      
        
    }
    return render(request, 'general/team.html', context)

def blog(request):
    context = {
        'title' : 'Nova - Blog',
        'sub_title' : 'Blog',
      
    }
    return render(request, 'general/blog.html', context)

def contact(request):
    context = {
        'title' : 'Nova - Contact',
        'sub_title' : 'Contact',
      

    }
    return render(request, 'general/contact.html', context)

def portfolio_details(request):
    context = {
        'title' : 'Portfolio Details - HeroBiz',
        'sub_title' : 'Portfolio Details',
       

    }
    return render(request, 'general/portfolio-details.html', context)

def blog_details(request):
    context = {
        'title' : 'Nova - Blog',
        'sub_title' : 'Blog Details',
        
    }
    return render(request, 'general/blog-details.html', context)

def loginpage(request):
    context = {
        'title' : 'Nova - Login',
         'sub_title' : 'Login',
    }
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'INVALID EMAIL/PASSWORD')
            return redirect(reverse('login_page'))
        else:
            login(request, user)
            messages.success(request, 'ACCESS GRANTED!!')
            return redirect(reverse('dashboard'))
    return render(request, 'general/login.html', context)

def logoutpage(request):
    try:
        logout(request)
        messages.success(request, 'LOGGED OUT')
        return redirect(reverse('login_page'))
    except:
        pass
    return redirect(reverse('login_page'))

def dashboard(request):
    context = {
        'title' : 'Nova - Dashboard',
         'sub_title' : 'Dashboard',
    }
    return render(request, 'general/dashboard.html', context)

def registration(request):
    form = CustomUserForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'title' : 'Nova - Register',
        'sub_title' : 'Register',
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('login_page'))
    return render(request, 'general/registration.html', context)
