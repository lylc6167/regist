from django.db import models
from organization.models import Merchant


class Info(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    goods = models.CharField(max_length=128,default='6167')
    number = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=128,default='6167')
    other = models.CharField(max_length=128,default='6167')


