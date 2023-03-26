from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers.change_log import ChangeLogSerializer

from apps.change_log.models import ChangeLog

class BooksListCreate(ListCreateAPIView):
    queryset = ChangeLog.objects.all()
    serializer = ChangeLogSerializer()
    

class BookUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = ChangeLog.objects.all()
    serializer = ChangeLogSerializer()
    lookup_field = 'pk'