from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from authz.permissions import HasAdminPermission
from .models import SampleEvent, SoilSampleDepthList, SamplesSoil, SoilExtraction, SampleSoilResults
from .serializers import SampleEventSerializer, SoilSampleDepthListSerializer, SamplesSoilSerializer, SoilExtractionSerializer, SampleSoilResultsSerializer, SampleEventSoilDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class SampleEventViewSet(viewsets.ModelViewSet):
    queryset = SampleEvent.objects.filter()
    serializer_class = SampleEventSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
       'date': ['exact', 'lte', 'gte'],
       'organization': ['exact'],
       'field': ['exact'],
       'field__farm': ['exact'],
       'field__farm__grower': ['exact'],
       'has_results':['exact'],
       'type':['exact'],
   } 
    ordering_fields = ['date']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('-date')
        return queryset

class SampleEventSoilDetailSerializerViewSet(viewsets.ModelViewSet):
    queryset = SampleEvent.objects.filter()
    serializer_class = SampleEventSoilDetailSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        queryset = queryset.filter(account__id=account_id)
        return queryset


class SoilSampleDepthListViewSet(viewsets.ModelViewSet):
    queryset = SoilSampleDepthList.objects.filter()
    serializer_class = SoilSampleDepthListSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

class SoilExtractionViewSet(viewsets.ModelViewSet):
    queryset = SoilExtraction.objects.filter()
    serializer_class = SoilExtractionSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

class SamplesSoilSerializerListViewSet(viewsets.ModelViewSet):
    queryset = SamplesSoil.objects.filter()
    serializer_class = SamplesSoilSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.kwargs.get('event')
        if event_id is not None:
            queryset = queryset.filter(sample_event_id=event_id).order_by('label')
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class SampleSoilResultsSerializerViewSet(viewsets.ModelViewSet):
    queryset = SampleSoilResults.objects.filter()
    serializer_class = SampleSoilResultsSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]

   
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)