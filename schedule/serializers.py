from rest_framework import serializers
from .models import Log, Schedule



class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('l','x','n')


class ScheduleSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('log','time_num', 'time_stamp', 'time_str')
