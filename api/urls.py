from django.urls import path
from .views import home, about, plan, logout_view, dashboard_view, signup_view, login_view, deposit

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('plan/', plan, name='plan'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('deposit/', deposit, name='deposit'),
]