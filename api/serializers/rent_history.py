from apps.rent_history.models import RentHistory
from rest_framework.serializers import ModelSerializer


class RentHistorySerializer(ModelSerializer):
    class Meta:
        model = RentHistory