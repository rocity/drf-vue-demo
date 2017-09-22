from rest_framework import serializers

from .models import List, Item


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class ItemSerializier(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
