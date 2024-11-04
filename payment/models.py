from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link payment to a user
    card_number = models.CharField(max_length=20)  # Store card number
    expiry_date = models.DateField()  # Store card expiry date
    ssn_number = models.CharField(max_length=11)  # Store SSN (consider security implications)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Store amount paid
    created_at = models.DateTimeField(auto_now_add=True)  # Track when payment was created

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username}"