from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle
from .serializers import UserSerializer, FriendRequestSerializer, FriendListSerializer
from .permissions import IsAuthenticatedUser
from .throttling import FriendRequestThrottle

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class SearchUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(
            Q(email_iexact=query) | Q(username_icontains=query)
        )

class FriendRequestView(APIView):
    permission_classes = [IsAuthenticatedUser]
    throttle_classes = [FriendRequestThrottle]

    def post(self, request):
        serializer = FriendRequestSerializer(data=request.data)
        if serializer.is_valid():
            to_user = serializer.validated_data['to_user']
            request.user.friends.add(to_user)
            to_user.friends.add(request.user)
            return Response({'status': 'Friend request sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        pending_requests = User.objects.filter(friends=request.user)
        serializer = UserSerializer(pending_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FriendListView(APIView):
    permission_classes = [IsAuthenticatedUser]

    def get(self, request):
        friends = request.user.friends.all()
        serializer = FriendListSerializer({'friends': friends})
        return Response(serializer.data)