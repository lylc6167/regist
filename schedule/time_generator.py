# 输入起始时间字符列表l，格式为'%Y-%m-%d %H:%M:%S'，时间间隔x秒,迭代次数n
# 生成三个时间列表，分别为时间绝对数，时间戳，时间字符串
# 检验数据 a=['2018-01-01 10:00:00','2018-01-01 12:00:00','2018-01-01 14:00:00'];b=7*24*3600;c=3
import time


class Num:

    list_num = []

    def __init__(self,l,x,n):
        self.l = l
        self.x = x
        self.n = n

        for time_str in self.l:
            time_num = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
            Num.list_num = sorted(Num.list_num + list(time_num + i * self.x for i in range(self.n)))



class Stamp(Num):

    def list_stamp(self):
        list_stamp = list(time.localtime(num) for num in Num.list_num)
        return list_stamp

class Str(Stamp):

    def list_str(self):
        list_str = list(time.strftime('%Y-%m-%d %H:%M:%S', stamp) for stamp in Stamp.list_stamp(self))
        return list_str
'''
    def tg_num(self,l, x, n):
        list_num = []
        for time_str in l:
            time_num = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
            list_num = sorted(list_num + list(time_num + i * x for i in range(n)))
        return list_num

    def tg_stamp(self,list_num):
        list_stamp = list(time.localtime(num) for num in list_num)
        return list_stamp

    def tg_str(self,list_stamp):

        list_str = list(time.strftime('%Y-%m-%d %H:%M:%S', stamp) for stamp in list_stamp)

        return list_str

'''