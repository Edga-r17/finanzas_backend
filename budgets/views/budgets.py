from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from budgets.models.budgets import Budget
from budgets.serializers.budgets import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    """CRUD de presupuestos"""
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
