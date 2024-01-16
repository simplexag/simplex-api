from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from authz.permissions import HasAdminPermission
from .models import Account, Organization, Grower, Farm, Field
from .serializers import AccountSerializer, OrganizationSerializer, GrowerSerializer, FarmSerializer, FieldSerializer, FieldLocationSerializer
from django_filters.rest_framework import DjangoFilterBackend


#@authentication_classes([])
#@permission_classes([IsAuthenticated])
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]

    
    def get_queryset(self):
        # Filter tasks based on the user's assignments
        #from authz.auth0_user import Auth0User

        #auth_user = Auth0User()
        #user_info = auth_user.get_user_info(self.request)
        #print (user_info["user_metadata"]["account"])
        #queryset = Account.objects.filter(owner=self.request.user)
        #return queryset
        
        user = str(self.request.user).split(" ")[1]
        return super().get_queryset().filter(owner=user)

    def perform_create(self, serializer):
        from authz.auth0_user import Auth0User
        instance = serializer.save()  # Save the object
        auth_user = Auth0User()
        data = {
            "account":str(instance.id)
        }
        user_info = auth_user.update_user_metadata(self.request,data)
        org = Organization()
        org.account = instance
        org.name = instance.name
        org.save()
        # Add your custom code here
        # This will be executed after the object is saved
        # You can access the instance object to perform any additional actions

        # For example:
        # instance.some_field = some_value
        # instance.save()

        return instance

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id)
        return queryset

class GrowerViewSet(viewsets.ModelViewSet):
    queryset = Grower.objects.filter()
    serializer_class = GrowerSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('name')
        return queryset
    
    def create(self, request, *args, **kwargs):
        # Check if the request data is a list
        is_many = isinstance(request.data, list)

        # If it's a list, serialize and create each object
        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Return the serialized data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.filter()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grower','grower__organization']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('name')
        return queryset
    
    def create(self, request, *args, **kwargs):
        # Check if the request data is a list
        is_many = isinstance(request.data, list)

        # If it's a list, serialize and create each object
        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Return the serialized data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.filter()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['farm']

    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id).order_by('name')
        return queryset

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list
        is_many = isinstance(request.data, list)

        # If it's a list, serialize and create each object
        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Return the serialized data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class FarmLocationList(generics.ListAPIView):

    queryset = Field.objects.filter()
    serializer_class = FieldLocationSerializer
    permission_classes = [IsAuthenticated, HasAdminPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['farm']
    def get_queryset(self):
        queryset = super().get_queryset()
        account_id = self.kwargs.get('account')
        if account_id is not None:
            queryset = queryset.filter(account__id=account_id)
        return queryset
