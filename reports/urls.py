from django.urls import path
from reports.views.reports import ReportViewSet

urlpatterns = [
    path('reports/', ReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='ReportView'),
    path('reports/<int:pk>/', ReportViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ReportDetailView'),
]
