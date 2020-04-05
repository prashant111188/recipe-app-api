from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUser(TestCase):

    def test_create_user_with_email_successful(self):
        """Test for creating user successfully"""
        email = "abc@xyz.com"
        password = "Testabc123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalize_emai(self):
        """Test for creating user and normalizing the email entered"""
        email = "abc@XYZ.COM"
        password = "test123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_create_user_with_email_validation(self):
        """Test for creating user and checking if email has been entered"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, "abc123")

    def test_create_superuser(self):
        """Test for checking creating super user workrs"""
        user = get_user_model().objects.create_superuser("abc@xyz.com", "abc123")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
