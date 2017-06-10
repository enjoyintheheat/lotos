from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from utils.process.image import main
from .models import Product
import math, os


def delete_file_from_storage(path):
    if os.path.isfile(path):
        os.remove(path)

@receiver(post_save, sender=Product)
def alter_image(sender, instance, created, **kwargs):
    main(
        instance.img.path,
        {
            'quantity': instance.quantity,
            'unit': instance.unit,
            'price': math.ceil(instance.price * (instance.percentage / 100))
        }
    )

@receiver(post_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    if instance.img:
        delete_file_from_storage(instance.img.path)
