from django.shortcuts import render
from .models import Log, Schedule
from .serializers import LogSerializer, ScheduleSerialzier
from rest_framework import viewsets
from rest_framework.response import Response
from .time_generator import Num, Stamp, Str


class GeneratorView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    # 在外键数据库操作子数据库

    def create(self, request, *args, **kwargs):
        l = [request.POST.get('l')]
        x = int(request.POST.get('x'))
        n = int(request.POST.get('n'))

        list_num = Num(l,x,n).list_num
        list_stamp = Stamp(l,x,n).list_stamp()
        list_str = Str(l,x,n).list_str()
        querysetlist = []
        for i in range(n):
            querysetlist.append(Schedule(
                time_num = list_num[i],
                time_stamp = list_stamp[i],
                time_str = list_str[i],
            ))
        Schedule.objects.bulk_create(querysetlist)

        return Response('create schedule success@!!!')

    def list(self, request, *args, **kwargs):
        return super(GeneratorView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(GeneratorView, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(GeneratorView, self).update(request, *args, **kwargs)

    def patrtial_update(self, request, *args, **kwargs):
        return super(GeneratorView, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(GeneratorView, self).destroy(request, *args, **kwargs)


class ScheduleViewSets(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerialzier



