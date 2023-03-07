from apps.task_librarian_detail.models import TaskLibrarianDetail
from rest_framework.serializers import ModelSerializer


class TaskLibrarianDetailSerializer(ModelSerializer):
    class Meta:
        model = TaskLibrarianDetail