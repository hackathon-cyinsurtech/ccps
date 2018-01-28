# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import viewsets

from api.models import Profile, IonicPushToken
from .serializers import UserSerializer, ProfileSerializer, IonicPushTokenSerializer
from .permissions import IsAuthenticatedOrCreateOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'patch']
    permission_classes = [IsAuthenticatedOrCreateOnly]

    def get_object(self):
        return self.request.user


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_user(self):
        return Profile.objects.first().user

    def get_object(self):
        return self.get_user().profile

    def get_serializer(self, *args, **kwargs):
        serializer = super(ProfileViewSet, self).get_serializer(*args, **kwargs)
        serializer.data['user'] = self.get_user()

        return serializer


class PushTokenViewSet(viewsets.ModelViewSet):
    serializer_class = IonicPushTokenSerializer
    queryset = IonicPushToken.objects.all()

    def get_user(self):
        return Profile.objects.first().user

    def get_object(self):
        return self.get_user().profile.ionicpushtoken_set.last()

    def get_serializer(self, *args, **kwargs):
        serializer = super(PushTokenViewSet, self).get_serializer(*args, **kwargs)

        # if self.request.POST:
        #     serializer.is_valid(raise_exception=True)
        #     serializer.validated_data['profile'] = self.get_user().profile

        return serializer
