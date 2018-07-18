from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import Profile,User,Country,Province

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #group = serializers.ReadOnlyField(source='group.name')
    class Meta:
        model = Profile
        fields = ('url','user','group','info_1','info_2','info_3')


class UserSerializer(serializers.ModelSerializer):
    #profile = serializers.HyperlinkedRelatedField(view_name='profile-detail',read_only=True)
    #group = serializers.ReadOnlyField(source='group.name')
    class Meta:
        model = User
        fields = ('url','username', 'password')

class GroupSerializer(serializers.ModelSerializer):
    #profile = serializers.HyperlinkedRelatedField(view_name='profile-detail', read_only=True)
    #user = serializers.HyperlinkedRelatedField(view_name='user_detail',read_only=True)
    class Meta:
        model = Group
        fields = ('url','id','name','permissions')






class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('url','id','name','area','code')

class ProvinceSerializer(serializers.ModelSerializer):
    #country = CountrySerializer()
    class Meta:
        model = Province
        fields = ('url','id','name','syscode','country')
    #def create(self, validated_data):
    #    country_data = validated_data.pop('country')
    #    province = Province.objects.create(**validated_data)
    #    Country.objects.create(province=province, **country_data)
    #    return province



'''
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'
        depth = 2


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('url','id','name','area','code')

'''
#class CountryNDSerializer(serializers.ModelSerializer):
#    province = ProvinceSerializer