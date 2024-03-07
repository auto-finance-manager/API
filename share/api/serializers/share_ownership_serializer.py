from rest_framework import serializers
from share.models import ShareOwnershipModel
from .share_serializer import ShareSerializer
from .slot_serializer import SlotSerializer


class ShareOwnershipSerializer(serializers.ModelSerializer):
    share = ShareSerializer(read_only=True)
    slots = SlotSerializer(read_only=True, many=True)

    class Meta:
        model = ShareOwnershipModel
        fields = '__all__'
