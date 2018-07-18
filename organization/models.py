from django.db import models


class Merchant(models.Model):
    info_1 = models.CharField(max_length=128, default='6167')
    info_2 = models.CharField(max_length=128, default='6167')
    info_3 = models.CharField(max_length=128, default='6167')