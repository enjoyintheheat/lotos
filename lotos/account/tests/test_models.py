from django.contrib.auth import get_user_model
from django.test import TestCase

class UserTest(TestCase):
    User = get_user_model()
    def setUp(self):
        self.user  = UserTest.User.objects.create_user(
            email='enjoy@gmail.com',
            password='qwerty123'
        )
        self.superuser = UserTest.User.objects.create_superuser(
            email='admin@gmail.com',
            password='qwerty'
        )

    def test_user(self):
        # user
        self.assertIsNotNone(self.user)
        self.assertEqual(self.user.email, 'enjoy@gmail.com')
        self.assertFalse(self.user.is_staff)
        # superuser
        self.assertIsNotNone(self.superuser)
        self.assertEqual(self.superuser.email, 'admin@gmail.com')
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_staff)
