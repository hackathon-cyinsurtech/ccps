import requests

from django.conf import settings

from api.models import IonicPushToken


class IonicApi(object):
    DEFAULT_SETTINGS = {
        'ios': {
            'priority': 10
        },
        'android': {
            'priority': 'high',
            'icon': 'notify'
        }
    }

    def emails_to_device_tokens(self, _):
        device_tokens = IonicPushToken.objects \
            .order_by('profile__user_id', '-modified_date') \
            .distinct('profile__user_id')

        return [x.token for x in device_tokens]

    def get_request_payload(self, title, message, tokens, payload):
        ios_settings = payload.pop('ios', self.DEFAULT_SETTINGS['ios'])
        android_settings = payload.pop('android', self.DEFAULT_SETTINGS['android'])

        data = {
            'tokens': tokens,
            'profile': settings.IONIC_SECURITY_PROFILE,
            'notification': {
                'title': title,
                'message': message,
                'payload': payload,
                'ios': ios_settings,
                'android': android_settings
            }
        }
        kwargs = {
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + settings.IONIC_AUTH_TOKEN
            }
        }

        return data, kwargs

    def notify(self, title, message, filters=None, **payload):
        success = ''
        errors = []
        warnings = []
        tokens = self.emails_to_device_tokens(filters)

        if not tokens:
            warnings.append('No users have registered tokens at this time.')
        else:
            data, kwargs = self.get_request_payload(title, message, tokens, payload)
            response = requests.post(settings.IONIC_HOST, json=data, **kwargs).json()

            if response.get('error', None):
                errors.append('{}: {}'.format(response['error']['type'], response['error']['message']))
            else:
                success = 'Status: {}\nRequest id: {}\nNotified device tokens: {}'.format(
                    response['meta']['status'],
                    response['meta']['request_id'],
                    ', '.join(response['data']['config']['tokens'])
                )

        return success, errors, warnings
