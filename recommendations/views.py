from django.shortcuts import render
from .models import RxEvent
from rest_framework import viewsets, generics, status
from .serializers import RxEventListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from authz.permissions import HasAdminPermission

class RxListViewSet(viewsets.ModelViewSet):
    queryset = RxEvent.objects.filter()
    serializer_class = RxEventListSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
       'created_at': ['exact', 'lte', 'gte'],
       'organization': ['exact'],
       'field': ['exact'],
       'field__farm': ['exact'],
       'field__farm__grower': ['exact'],
   } 
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('-created_at')
        return queryset
    
