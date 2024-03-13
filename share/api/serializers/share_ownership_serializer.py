from rest_framework import serializers
from share.models import ShareOwnershipModel
from .share_serializer import ShareSerializer
from .slot_serializer import SlotSerializer


class ShareOwnershipSerializer(serializers.ModelSerializer):
    share = ShareSerializer(read_only=True)
    slots = SlotSerializer(read_only=True, many=True)
    total_profit = serializers.SerializerMethodField()

    def get_total_profit(self, obj):
        remaining_lots = 0
        total_profit = 0

        # Her bir işlemi değerlendirme
        if slots := obj.slots.all():
            for transaction in slots:
                if transaction.progres_type == transaction.ProgresType.BUY:
                    remaining_lots += transaction.quantity
                else:
                    sold_lots = transaction.quantity
                    sale_price = float(transaction.price)

                    # Satılan lotlar için kar hesapla
                    profit = sold_lots * (sale_price - float(obj.share.current_price))
                    total_profit += profit

                    # Kalan lotları güncelle
                    remaining_lots -= sold_lots

            # Karı ve kalan lot sayısını yazdır
        print("Toplam Kar:", total_profit)
        print("Kalan Lot Sayısı:", remaining_lots)
        return total_profit

    class Meta:
        model = ShareOwnershipModel
        fields = '__all__'
