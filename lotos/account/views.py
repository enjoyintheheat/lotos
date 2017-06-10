from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import (
    View, TemplateView
)
from article.models import Article
from .forms import (
    UserChangeForm, UserCreationForm
)

class AccountSigninView(View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Вы успешно авторизовались на сайте.'
            )
        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Авторизоваться на сайте не удалось, '
                'проверьте правильность своей почты или пароля.'
            )
        return redirect(reverse('base:index'))

class AccountLogoutView(View):
    def get(self, request):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            'Вы вышли из своего профиля, текущая сессия была уничтожена.'
        )
        return redirect(reverse('base:index'))

class AccountSignupView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Вы успешно зарегистрировали аккаунт. '
                'Зайдите под своей почтой и паролем.'
            )
        else:
            messages.add_message(
                request,
                messages.WARNING,
                form.errors
            )
        return redirect(reverse('base:index'))

class AccountDetailView(TemplateView):
    template_name = 'account/detail.html'
    User = get_user_model()

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context['account'] = self.User.objects.get(email=kwargs['email'])
        context['articles'] = Article.objects.filter(
            user__email=kwargs['email']
        )

        return context
