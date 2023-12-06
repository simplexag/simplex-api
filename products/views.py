from rest_framework import viewsets, mixins, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authz.permissions import HasAdminPermission

from .models import AccountProducts
from .serializers import AccountProductsListSerializer, AccountProductsDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class AccountProductsListSerializerViewSet(viewsets.ModelViewSet):
    queryset = AccountProducts.objects.filter()
    serializer_class = AccountProductsListSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        queryset = queryset.filter(account__id=account_id)
        return queryset


class AccountProductsDetailSerializer(viewsets.ModelViewSet):
    queryset = AccountProducts.objects.filter()
    serializer_class = AccountProductsDetailSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        queryset = queryset.filter(account__id=account_id)
        return queryset