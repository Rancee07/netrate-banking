from django import forms
from .models import Transaction, Loan

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount', 'transaction_type']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'due_date']
