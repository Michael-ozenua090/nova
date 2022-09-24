from django.shortcuts import render

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
