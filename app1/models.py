from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_app.models import CustomUserModel

# Create your models here.
class categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class product(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='product_list')
    price = models.IntegerField(null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Added_by(models.Model):
    user = models.CharField(max_length=50)
    items = models.ForeignKey(product, on_delete=models.CASCADE, related_name='user_list')

    def __str__(self):
        return str(self.user)


class event(models.Model):
    created = models.CharField(max_length=100)
    by_user = models.ForeignKey(Added_by, on_delete=models.CASCADE)

    def __str__(self):
        return self.created +'--'+ str(self.by_user)


@receiver(post_save, sender=Added_by)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        event.objects.create(created=("product created - %s"%('instance.items')),
                             by_user=instance)