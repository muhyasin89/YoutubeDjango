from rest_framework.serializers import ModelSerializer

from apps.change_log.models import ChangeLog


class ChangeLogSerializer(ModelSerializer):
    def to_internal_value(self, data):
   

        return super(ChangeLogSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        data = super(ChangeLogSerializer, self).to_representation(instance)

        return data

    class Meta:
        model = ChangeLog