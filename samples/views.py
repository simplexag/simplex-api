from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from authz.permissions import HasAdminPermission
from .models import SampleEvent, SoilSampleDepthList
from .serializers import SampleEventSerializer, SoilSampleDepthListSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SampleEventViewSet(viewsets.ModelViewSet):
    queryset = SampleEvent.objects.filter()
    serializer_class = SampleEventSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization','field','field__farm','field__farm__grower']
    ordering_fields = ['date']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('name')
        return queryset

class SoilSampleDepthListViewSet(viewsets.ModelViewSet):
    queryset = SoilSampleDepthList.objects.filter()
    serializer_class = SoilSampleDepthListSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']