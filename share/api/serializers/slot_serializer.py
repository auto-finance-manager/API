from rest_framework import serializers
from share.models import SlotModel


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotModel
        fields = '__all__'

