from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class SocialNetworkTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_signup(self):
        response = self.client.post('/api/signup/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_user(self):
        response = self.client.get('/api/search/?q=test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_friend_request(self):
        new_user = User.objects.create_user(username='newuser', email='newuser@example.com', password='newpass')
        response = self.client.post('/api/friend-request/', {'to_user': new_user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_friend_list(self):
        response = self.client.get('/api/friends/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)