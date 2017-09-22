from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import List, Item
from .serializers import ListSerializer, ItemSerializer


class ListViewSet(viewsets.ModelViewSet):
    """Viewset for lists
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.AllowAny, ]


class ItemViewSet(viewsets.ModelViewSet):
    """Viewset for items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny, ]
