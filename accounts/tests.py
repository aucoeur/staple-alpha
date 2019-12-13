from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your tests here.

class UserTestCase(TestCase):

    def test_good_login(self):
        user = User.objects.create_user("user", password="password")
        auth_user = authenticate(username="user", password="password")
        self.assertTrue(auth_user is not None)
        self.assertEqual(user.pk, auth_user.pk)

    def test_bad_login(self):
        authed_user = authenticate(username="faker", password="password")
        self.assertTrue(authed_user is None)