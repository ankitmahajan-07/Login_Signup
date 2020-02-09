from rest_framework.serializers import ModelSerializer
from mates.models import signup

class UserListSerializer(ModelSerializer):
    class Meta:
        model = signup
        fields = [
            'id',
            'Username',
            'Password'
        ]

class RetrieveUserSerializer(ModelSerializer):
    class Meta:
        model = signup
        fields = [
            'id',
            'Username',
            'Password'
        ]