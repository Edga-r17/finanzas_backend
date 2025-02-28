from django.urls import path
from transactions.views.transactions import TransactionViewSet

urlpatterns = [
    path('transactions/', TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='TransactionView'),
    path('transactions/<int:pk>/', TransactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='TransactionDetailView'),
]
