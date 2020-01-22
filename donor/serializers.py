from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Donor


# serializer class for creating a donr full details.
class DonorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor
        fields = [
            'full_name', 'mobile_number', 'address', 'age',
            'blood_group', 'owner'
        ]


# serializer class for donorListing
class DonorListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(source='username')

    class Meta:
        model = Donor
        fields = [
            'full_name',
            'mobile_number',
            'address',
            'age',
            'blood_group',
            'owner'
        ]

    def get_owner(self, obj):
        return obj.owner.username


# serializer class for user details and donor details
class UserSerializer(serializers.ModelSerializer):
    details = DonorListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'details'
        ]
