from rest_framework import serializers
from share.models import ShareOwnershipModel
from .share_serializer import ShareSerializer
from .slot_serializer import SlotSerializer


class ShareOwnershipSerializer(serializers.ModelSerializer):
    share = ShareSerializer(read_only=True)
    slots = SlotSerializer(read_only=True, many=True)
    general_status = serializers.SerializerMethodField()

    @staticmethod
    def get_general_status(obj):
        remaining_lots = 0
        total_profit = 0
        if slots := obj.slots.all():
            for transaction in slots:
                if transaction.progres_type == transaction.ProgresType.BUY:
                    remaining_lots += transaction.quantity
                else:
                    sold_lots = transaction.quantity
                    sale_price = float(transaction.price)
                    profit = sold_lots * (sale_price - float(obj.share.current_price))
                    total_profit += profit
                    remaining_lots -= sold_lots
        return {
            'total_profit': total_profit,
            'remaining_lots': remaining_lots
        }

    class Meta:
        model = ShareOwnershipModel
        fields: str = '__all__'
