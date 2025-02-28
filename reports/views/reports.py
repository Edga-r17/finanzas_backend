from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from reports.models.reports import Report
from reports.serializers.reports import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """CRUD de reportes financieros"""
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)
