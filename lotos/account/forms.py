from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm, ReadOnlyPasswordHashField
)

class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'aria-describedby': 'email-login',
                'placeholder': 'mymail@example.com'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'aria-describedby': 'password-login',
                'placeholder': 'Не менее 8 символов'
            })
        }

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label='Пароль',
        widget=forms.PasswordInput(),
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_password(self):
        return self.initial['password']

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'password1-signup',
            'placeholder': 'Не менее 8 символов'
        })
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'password2-signup',
            'placeholder': 'Не менее 8 символов'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'aria-describedby': 'email-signup',
                'placeholder': 'mymail@example.com'
            })
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValueError('Пароли не совпадают.')

        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user
