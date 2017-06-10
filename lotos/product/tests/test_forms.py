from django.test import TestCase
from product.forms import ProductForm
from product.models import Product

class ProductFormTest(TestCase):
    def setUp(self):
        self.product = {
            'name': 'product',
            'quantity': 2,
            'unit': 'кг',
            'price': 60,
            'percentage': 100
        }
        self.form_add = ProductForm(data=self.product)

    def test_form(self):
        # temp
        self.assertFalse(self.form_add.is_valid())
