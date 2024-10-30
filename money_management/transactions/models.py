from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_transactions")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPES = [('send', 'Send'), ('receive', 'Receive')]
    transaction_type = models.CharField(choices=TRANSACTION_TYPES, max_length=10)

class Loan(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('pending', 'Pending')], default='pending')
    due_date = models.DateField()
