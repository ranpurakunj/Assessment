from django.db import models
from django.conf import settings

# from accounts.models import CustomUser
# Create your models here.

class Cafe(models.Model):
    c_id = models.PositiveIntegerField(primary_key=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    m_id = models.PositiveIntegerField(null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return "Cafe ID "+ str(self.c_id)

class StoreOrders(models.Model):
    order_date= models.DateField(null=True, blank=True)
    bill_amount = models.PositiveIntegerField(null=True, blank=True)
    cafe_id = models.ForeignKey(Cafe, on_delete=models.CASCADE, to_field='c_id', related_name='+')
    manager_id = models.ForeignKey(Cafe, on_delete=models.CASCADE, to_field='m_id', related_name='managerid+')