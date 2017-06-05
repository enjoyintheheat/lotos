from account.forms import (
    LoginForm, UserChangeForm, UserCreationForm
)
from django.test import TestCase

class FormsTest(TestCase):
    def setUp(self):
        login_data = {
            'email': 'enjoy@gmail.com',
            'password': 'qwerty123'
        }
        self.login_form = LoginForm(data=login_data)
        change_data = {
            'email': 'enjoy@gmail.com',
            'password': 'qwert23'
        }
        self.change_form = UserChangeForm(
            data={
                'email': change_data['email']
            },
            initial={
                'password': change_data['password']
            }
        )
        create_data = {
            'email': 'check@yandex.ru',
            'password1': '123rty',
            'password2': '123rty'
        }
        self.create_form = UserCreationForm(
            data=create_data
        )

    def test_forms(self):
        self.assertTrue(self.login_form.is_valid())
        self.assertTrue(self.change_form.is_valid())
        self.assertTrue(self.create_form.is_valid())
