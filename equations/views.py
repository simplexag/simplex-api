from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from authz.permissions import HasAdminPermission
from .models import EquationSets, EquationCrops, EquationElement, StandardSoilRxElements, StandardRxCrops
from .serializers import EquationSetsListSerializer, EquationElementDetailSerializer, StandardSoilRxElementsSerializer, StandardRxCropsSerializer, EquationSetsSerializer, EquationCropsSerializer, EquationElementSerializer, EquationCropsOnlySerializer, EquationElementOnlySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

class StandardSoilRxElementsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = StandardSoilRxElements.objects.filter()
    serializer_class = StandardSoilRxElementsSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

class StandardRxCropsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = StandardRxCrops.objects.filter()
    serializer_class = StandardRxCropsSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']

class EquationSetsViewSet(viewsets.ModelViewSet):
    queryset = EquationSets.objects.filter()
    serializer_class = EquationSetsSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    filterset_fields = ['organization']
    ordering_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        queryset = queryset.filter(account__id=account_id)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EquationCropsViewSet(viewsets.ModelViewSet):
    queryset = EquationCrops.objects.filter()
    serializer_class = EquationCropsOnlySerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]

    def get_queryset(self):
        queryset = super().get_queryset()
        set_id = self.kwargs.get('set')
        queryset = queryset.filter(set__id=set_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EquationElementViewSet(viewsets.ModelViewSet):
    queryset = EquationElement.objects.filter()
    serializer_class = EquationElementOnlySerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]

    def get_queryset(self):
        queryset = super().get_queryset()
        crop_id = self.kwargs.get('crop')
        queryset = queryset.filter(crop__id=crop_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EquationSetsSerializerViewSet(viewsets.ModelViewSet):
    queryset = EquationSets.objects.filter()
    serializer_class = EquationSetsListSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get']
    filterset_fields = ['organization']
    ordering_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        queryset = queryset.filter(account__id=account_id)
        return queryset

class EquationElementDetailViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = EquationElement.objects.filter()
    serializer_class = EquationElementDetailSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    http_method_names = ['get','post','patch','delete']
   
