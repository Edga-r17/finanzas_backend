from django.db import models
from django.contrib.auth import get_user_model
from _base.models import BaseModel

User = get_user_model()

CATEGORY_CHOICES = [
        ('income', 'Ingreso'),
        ('expense', 'Gasto'),
    ]
class Transaction(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.amount}"
