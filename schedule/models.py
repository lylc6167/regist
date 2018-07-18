from django.db import models
import time


class Log(models.Model):
    l = models.CharField('时间列表的字符串元组', max_length=32, default='2018-01-01 00:00:00')
    x = models.IntegerField('差值')
    n = models.IntegerField('迭代次数')


class Schedule(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, default=1)

    time_num = models.IntegerField('时间值')  # 格林威治时间秒数
    time_stamp = models.DateTimeField('时间戳')
    time_str = models.CharField('时间字符', max_length=32, default='2018-01-01 00:00:00')

    class Meta:
        ordering = ['time_stamp']