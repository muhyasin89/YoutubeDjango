

from api.serializers.task_librarian import TaskLibrarianSerializer
from apps.task_librarian.models import TaskLibrarian
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TaskLibrariansListCreate(ListCreateAPIView):
    queryset = TaskLibrarian.objects.all()
    serializer = TaskLibrarianSerializer()
    

class TaskLibrarianUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = TaskLibrarian.objects.all()
    serializer = TaskLibrarianSerializer()
    lookup_field = 'pk'