from django.conf import settings
from django.db import models

class Article(models.Model):
    caption = models.CharField(db_index=True, max_length=256, verbose_name='Заголовок статьи')
    body = models.TextField(max_length=5000, verbose_name='Тело статьи')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']
