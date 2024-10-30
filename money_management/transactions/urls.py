from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('transaction/', views.transaction_view, name='transaction'),
    path('loan/', views.loan_view, name='loan'),
    path('', views.home, name='home'),
]
