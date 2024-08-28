from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class FriendRequestSerializer(serializers.Serializer):
    to_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

class FriendListSerializer(serializers.Serializer):
    friends = UserSerializer(many=True)