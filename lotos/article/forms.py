from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ArticleForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        article = super(ArticleForm, self).save(commit=False)
        if self.user is None or not self.user.is_authenticated:
            raise forms.ValidationError(
                'Пользователь неопределен или не аутентифицирован.'
            )
        article.user = self.user
        if commit:
            article.save()

        return article

    class Meta:
        model = Article
        fields = ('caption', 'body')
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-describedby': 'dashboard-article-caption',
                'placeholder': 'Не более 64 символов'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-describedby': 'dashboard-body-caption',
                'placeholder': 'Не более 5000 символов'
            })
        }
