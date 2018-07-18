from django.shortcuts import render
from django.contrib.auth.models import User,Group
from user.models import Profile
from user.serializers import UserSerializer,ProfileSerializer,GroupSerializer
from user.permissions import IsUserOrReadOnly
from rest_framework import viewsets, renderers, request,generics,mixins,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.decorators import permission_required

from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from user.models import Country,Province
from user.serializers import CountrySerializer, ProvinceSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegisterView(viewsets.ModelViewSet ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        #group = request.POST.get('group')
        User.objects.create_user(username=username,
                                 password=password)

        #User.groups.add(group)
        return Response('create user success!!')

    def patrtial_update(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')
    def list(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')
    def retrieve(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')

    def update(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')
    def destroy(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly)

    # 在子数据库操作外键数据库

    def create(self, request, *args, **kwargs):
        #成功加入组
        user = self.request.user
        group_id = request.POST.get('group')  # 此处显示的是str链接
        group_id = int(group_id)
        group = Group.objects.get(id=group_id)
        user.groups.add(group)
        user.save()
        #保存数据
        Profile.objects.create(
            user_id=user.id,
            info_1=request.POST.get('info_1'),
            info_2=request.POST.get('info_2'),
            info_3=request.POST.get('info_3'),
        ).group.add(group_id)

        return Response('Join group and save data!!')

    def patrtial_update(self, request, *args, **kwargs):
        '''
        1、在创建一个新的的时候：
        p1=Post.objects.create(title=title,content=content,pub_date=pub_date,author=author)
        p1.label.add(p)
        其中label是ManyToMany 字段。
        2、更新的时候：
        p1=Post.objects.filter(id=num).save(title=title,content=content,pub_date=pub_date,author=author)
        3、如果此时误用update，则成了批量更新，会发生错误。
        '''
        return Response('Error, No  such way!!')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')

    def update(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')
    def destroy(self, request, *args, **kwargs):
        return Response('Error, No  such way!!')

class AccountView(viewsets.ModelViewSet):  # 实际就是UserViewSet
    queryset = User.objects.all()
    serializer_class = UserSerializer


    #def put(self,request,*args,**kwargs):
    #    username = request.POST.get('username')
    #    new_password = request.POST.get('password')
    #    User.objects.get(username).set_password(raw_password=new_password)

    #    return Response('update password success!!')


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
'''
    def create(self, request, *args, **kwargs):
        return super(ViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(ViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ViewSet, self).update(request, *args, **kwargs)

    def patrtial_update(self, request, *args, **kwargs):
        return super(ViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ViewSet, self).destroy(request, *args, **kwargs)
'''


