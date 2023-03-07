from api.serializers.task_report import TaskReportSerializer
from apps.task_report.models import TaskReport
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TaskReportsListCreate(ListCreateAPIView):
    queryset = TaskReport.objects.all()
    serializer = TaskReportSerializer()
    

class TaskReportUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = TaskReport.objects.all()
    serializer = TaskReportSerializer()
    lookup_field = 'pk'