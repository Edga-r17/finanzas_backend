from rest_framework import viewsets, permissions
from transactions.models.transactions import Transaction
from transactions.serializers.transactions import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
    CRUD de transacciones (ingresos y gastos).
    Solo accesible para usuarios autenticados.
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
