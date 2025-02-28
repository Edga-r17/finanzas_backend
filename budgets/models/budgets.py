from django.db import models
from django.contrib.auth import get_user_model
from _base.models import BaseModel

User = get_user_model()

class Budget(BaseModel):
    """
    Modelo para la gestión de presupuestos de usuarios.
    Permite asignar un límite de gasto a una categoría específica.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)  
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.limit}"
