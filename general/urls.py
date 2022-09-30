from django.urls import path
from general.views import blog, blog_details, contact, dashboard, homepage, about, loginpage, logoutpage, portfolio, portfolio_details, registration, services, team

urlpatterns = [
path('', homepage, name='homepage'),
path('about', about, name='about_us'),
path('services', services, name='services'),
path('portfolio', portfolio, name='portfolio'),
path('team', team, name='team'),
path('blog', blog, name='blog'),
path('contact', contact, name='contact'),
path('portfollio/details', portfolio_details, name='portfolio_details'),
path('blog/details', blog_details, name='blog_details'),
path('login', loginpage, name='login_page'),
path('logout',logoutpage, name='logout_page' ),
path('dashboard', dashboard, name='dashboard'),
path('registration', registration, name='registration_page')


]
