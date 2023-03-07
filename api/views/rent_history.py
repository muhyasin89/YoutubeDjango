

from api.serializers.rent_history import RentHistorySerializer
from apps.rent_history.models import RentHistory
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class RentHistoriesListCreate(ListCreateAPIView):
    queryset = RentHistory.objects.all()
    serializer = RentHistorySerializer()
    

class RentHistoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = RentHistory.objects.all()
    serializer = RentHistorySerializer()
    lookup_field = 'pk'