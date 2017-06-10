from django.contrib.auth import get_user_model
from django.test import TestCase
from article.models import Article

class ArticleTest(TestCase):
    User = get_user_model()
    def setUp(self):
        self.user = ArticleTest.User.objects.create_user(
            email='newsmaker@mail.ru',
            password='123qwerty'
        )
        self.article = Article.objects.create(
            caption='Моя статья',
            body='test',
            user=self.user
        )

    def test_article(self):
        self.assertIsNotNone(self.article)
        self.assertEqual(self.article.caption, 'Моя статья')
        self.assertEqual(self.article.body, 'test')
        self.assertEqual(self.article.user.email, 'newsmaker@mail.ru')
        self.assertIsNotNone(self.article.date)
