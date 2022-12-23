from rest_framework import serializers

from .models import Cafe, StoreOrders

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "c_id",
            "manager",
            "m_id",
        )
        model = Cafe

class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "order_date",
            "bill_amount",
            "cafe_id",
            "manager_id",
        )