from api.serializers.task_librarian_detail import TaskLibrarianDetailSerializer
from api.serializers.task_report import TaskReportSerializer
from apps.task_librarian.models import TaskLibrarian
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.core import serializers

class TaskLibrarianSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super(TaskLibrarianSerializer, self).to_representation(instance)
        # get all task detail
        record_task_detail = instance.task_detail.all() if instance.task_detail.count() else None
        if record_task_detail:
            record_task_detail = serializers.serialize('json', record_task_detail)
            
        data['task_detail'] = record_task_detail


        #get all task report
        record_task_report = instance.report.all() if instance.report.count() else None
        if record_task_report:
            record_task_report = serializers.serialize('json', record_task_report)

        data['task_report'] = record_task_report

        return data

    class Meta:
        model = TaskLibrarian
        exclude = ('author','report',)