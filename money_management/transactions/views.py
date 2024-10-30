from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Transaction, Loan
from .forms import TransactionForm, LoanForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to admin if the user is a superuser
            if user.is_superuser:
                return redirect('/admin/')  # Redirect to admin
            return redirect('home')  # Otherwise redirect to home or dashboard
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def transaction_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.sender = request.user
            transaction.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'transaction.html', {'form': form})

@login_required
def loan_view(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.borrower = request.user
            loan.save()
            return redirect('home')
    else:
        form = LoanForm()
    return render(request, 'loan.html', {'form': form})
def home(request):
    return render(request, 'home.html')