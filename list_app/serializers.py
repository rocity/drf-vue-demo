from rest_framework import serializers

from .models import List, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = ('title', 'id', 'items', )

    def get_items(self, obj):
        return ItemSerializer(obj.items.all(), many=True).data
