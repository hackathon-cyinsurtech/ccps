# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db.models import Avg, Sum
from django.db.models.functions import TruncDay
from rest_framework import serializers

from api.models import Metric, Profile, IonicPushToken


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        read_only_fields = ('id',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # These should support writes + add bmi from (age, gender, weight, height)
    gender = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    # end comment
    steps = serializers.SerializerMethodField()
    heart_rate = serializers.SerializerMethodField()

    def get_gender(self, instance):
        return Profile.GENDERS[instance.gender][1]

    def get_weight(self, instance):
        obj = instance.metric_set.filter(name=2).last()
        return obj.value if obj else 'n/a'

    def get_height(self, instance):
        obj = instance.metric_set.filter(name=3).last()
        return obj.value if obj else 'n/a'

    def get_steps(self, instance):
        return instance.metric_set \
            .filter(name=0) \
            .annotate(day=TruncDay('timestamp')) \
            .values('day') \
            .annotate(total=Sum('value')) \
            .values_list('day', 'total')

    def get_heart_rate(self, instance):
        return instance.metric_set \
            .filter(name=1) \
            .annotate(day=TruncDay('timestamp')) \
            .values('day') \
            .annotate(average=Avg('value')) \
            .values_list('day', 'average')

    class Meta:
        model = Profile
        fields = ('user', 'age', 'gender', 'weight', 'height', 'bmi', 'steps', 'heart_rate')


class IonicPushTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = IonicPushToken
        fields = '__all__'
