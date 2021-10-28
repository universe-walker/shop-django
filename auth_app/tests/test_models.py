from django.test import TestCase

from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(email='mytest@gmail.com',
                                        first_name='Anton',
                                        last_name='Ivanov')

    def test_first_name_verbose_name(self):
        user = self.User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'имя')

    def test_last_name_verbose_name(self):
        user = self.User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'фамилия')

    def test_email_verbose_name(self):
        user = self.User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_first_name_max_length(self):
        user = self.User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 40)

    def test_last_name_max_length(self):
        user = self.User.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 40)

    def test_username_is_none(self):
        user = self.User.objects.get(id=1)
        username = user.username
        self.assertIsNone(username)

    def test_email_max_length(self):
        user = self.User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)

    def test_str(self):
        user = self.User.objects.get(id=1)
        self.assertEquals(str(user), 'mytest@gmail.com')

    def test_repr(self):
        user = self.User.objects.get(id=1)
        self.assertEquals(repr(user), 'mytest@gmail.com')
