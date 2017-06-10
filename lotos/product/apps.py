from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'
    verbose_name = 'Продажа'

    def ready(self):
        import product.signals
