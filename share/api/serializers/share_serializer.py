from share.models import ShareModel
from rest_framework import serializers


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareModel
        fields: str = '__all__'

