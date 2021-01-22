from rest_framework import serializers
from ..models import StoreFront

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreFront
        fields = ('uuid', 'name', 'latitude', 'longitude', 'street_address', 'slug')