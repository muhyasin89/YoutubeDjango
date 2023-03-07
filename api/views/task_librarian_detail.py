

from api.serializers.task_librarian_detail import TaskLibrarianDetailSerializer
from apps.task_librarian_detail.models import TaskLibrarianDetail
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TaskLibrarianDetailsListCreate(ListCreateAPIView):
    queryset = TaskLibrarianDetail.objects.all()
    serializer = TaskLibrarianDetailSerializer()
    

class TaskLibrarianDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = TaskLibrarianDetail.objects.all()
    serializer = TaskLibrarianDetailSerializer()
    lookup_field = 'pk'