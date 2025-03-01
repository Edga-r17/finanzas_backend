from rest_framework import serializers
from budgets.models.budgets import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'