from apps.task_report.models import TaskReport
from rest_framework.serializers import ModelSerializer


class TaskReportSerializer(ModelSerializer):
    class Meta:
        model = TaskReport