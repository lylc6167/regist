from django.db import models
from django.contrib.auth.models import Group,AbstractUser,User,UserManager


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    group = models.ManyToManyField(Group, default='6167')
    info_1 = models.CharField(max_length=128,default='6167')
    info_2 = models.CharField(max_length=128,default='6167')
    info_3 = models.CharField(max_length=128,default='6167')



class Country(models.Model):
    name = models.CharField(max_length=64, default='6167')
    area = models.CharField(max_length=64, default='6167')
    code = models.CharField(max_length=64, default='6167')


class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default='6167')
    syscode = models.CharField(max_length=64, default='6167')


#class C(models.Model):
#    b = models.ForeignKey(B, on_delete=models.CASCADE)
#    h = models.CharField(max_length=64, default='6167')
#    i = models.CharField(max_length=64, default='6167')

#class Manager(models.Model):
#    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
#    group = models.ForeignKey(Group, on_delete=models.CASCADE)


#class Casher(models.Model):
#    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
#    group = models.ForeignKey(Group, on_delete=models.CASCADE)


#class Customer(models.Model):
#    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    group = models.ForeignKey(Group, on_delete=models.CASCADE)



