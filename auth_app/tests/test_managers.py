from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTest(TestCase):
    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(email='testemail@gmail.com', password="qwerty1")

    def test_email(self):
        user = self.User.objects.get(id=1)
        self.assertEquals(user.email, 'testemail@gmail.com')

    def test_without_args(self):
        with self.assertRaises(TypeError):
            self.User.objects.create_user()

    def test_empty_email_without_password(self):
        """Email is empty string and password isn't specified"""
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email='')

    def test_empty_email(self):
        """Email is empty"""
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email='', password='qwerty2')


class CustomUserManagerSuperuserCreationTest(TestCase):
    """Test for CustomUserManager superuser creation"""
    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_superuser(
            email='superuser@gmail.com',
            password='qwerty3'
        )

    def test_email(self):
        admin_user = self.User.objects.get(id=1)
        self.assertEquals(admin_user.email, 'superuser@gmail.com')

    def test_is_active(self):
        admin_user = self.User.objects.get(id=1)
        self.assertTrue(admin_user.is_active)

    def test_is_staff(self):
        admin_user = self.User.objects.get(id=1)
        self.assertTrue(admin_user.is_staff)

    def test_is_superuser(self):
        admin_user = self.User.objects.get(id=1)
        self.assertTrue(admin_user.is_superuser)

    def test_username_is_none(self):
        admin_user = self.User.objects.get(id=1)
        self.assertIsNone(admin_user.username)

    def test_superuser_exception_admin_is_false(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='superuser@gmail.com',
                password='qwerty123',
                is_superuser=False
            )

    def test_superuser_exception_staff_is_false(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='superuser@gmail.com',
                password='qwerty123',
                is_staff=False
            )
