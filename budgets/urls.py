from django.urls import path
from budgets.views.budgets import BudgetViewSet

urlpatterns = [
    path('budgets/', BudgetViewSet.as_view({'get': 'list', 'post': 'create'}), name='BudgetView'),
    path('budgets/<int:pk>/', BudgetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='BudgetDetailView'),
]
