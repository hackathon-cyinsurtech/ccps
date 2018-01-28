# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import math

from django.contrib.auth.models import User
from django.db import models


class DatedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    modified_date = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        abstract = True


class Profile(DatedModel):
    GENDERS = (
        (0, 'male'),
        (1, 'female'),
    )

    PROVIDERS = (
        (0, 'garmin'),
    )

    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.SmallIntegerField(choices=GENDERS)
    external_id = models.CharField(max_length=100, blank=True, default=123)
    provider = models.SmallIntegerField(choices=PROVIDERS, blank=True, default=0)

    @property
    def bmi(self):
        weight = self.metric_set.filter(name=2).last().value
        height = self.metric_set.filter(name=3).last().value / float(100)
        return int(math.ceil(weight / (height ** 2)))

    def __unicode__(self):
        return '{}'.format(self.user)


class Metric(DatedModel):
    # Variable: Steps, Heart rate
    # Semi-variable: Weight, Height

    DATA_TYPES = (
        (0, 'integer'),
        (1, 'float'),
    )
    METRIC_TYPES = (
        (0, 'steps'),
        (1, 'heart_rate'),
        (2, 'weight'),
        (3, 'height'),
    )

    profile = models.ForeignKey(Profile)
    name = models.SmallIntegerField(choices=METRIC_TYPES)
    value = models.SmallIntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    data_type = models.SmallIntegerField(choices=DATA_TYPES, default=0)

    def __unicode__(self):
        return '{}\'s {}: {}'.format(self.profile, self.name, self.value)


class IonicPushToken(DatedModel):
    profile = models.ForeignKey(Profile)
    token = models.CharField(max_length=200)
