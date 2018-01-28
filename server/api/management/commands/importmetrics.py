from django.core.management.base import BaseCommand

from api.models import Profile, Metric


class Provider(object):
    code = None

    def get_metrics(self, profile):
        raise NotImplementedError()


class Garmin(Provider):
    code = 0

    def get_metrics(self, profile):
        return [
            Metric(profile=profile, name='', value=0),
        ]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for profile in Profile.objects.all():
            provider = {
                0: Garmin()
            }[profile.provider]

            for metric in provider.get_metrics(profile):
                metric.save()
