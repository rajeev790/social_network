from django.urls import path
from .views import SignupView, SearchUserView, FriendRequestView, FriendListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('search/', SearchUserView.as_view(), name='search'),
    path('friend-request/', FriendRequestView.as_view(), name='friend_request'),
    path('friends/', FriendListView.as_view(), name='friend_list'),
]