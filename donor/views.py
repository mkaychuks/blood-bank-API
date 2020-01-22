from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .serializers import (
    UserSerializer, DonorListSerializer, DonorCreateSerializer
)
from .models import Donor
from .permissions import IsAuthorOrReadOnly


# views for listing the Users
class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


# view handling the profile of the logged-in user
class UserDetail(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# view handling the ability to create donor details/editable
class DonorEditDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonorCreateSerializer
    queryset = Donor.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,)


class DonorCreateDetails(generics.CreateAPIView):
    serializer_class = DonorCreateSerializer
    queryset = Donor.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,)


# view handling the list of donors
class DonorList(generics.ListAPIView):
    serializer_class = DonorListSerializer

    def get_queryset(self):
        queryset = Donor.objects.order_by('-owner')
        return queryset
