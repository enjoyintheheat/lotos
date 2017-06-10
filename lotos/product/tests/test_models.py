from django.test import TestCase
from product.models import Product

class ProductTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Продукт',
            quantity=2,
            price=60
        )

    def test_model(self):
        self.assertIsNotNone(self.product)
        self.assertEqual(self.product.name, 'Продукт')
        self.assertEqual(self.product.quantity, 2)
        self.assertEqual(self.product.price, 60)
