from django.views.generic import FormView

from api.admin.apis import IonicApi
from api.admin.forms import NotificationsIonicForm


class NotificationsIonic(FormView):
    SUPPORTED_PAYLOAD_KEYS = []

    template_name = 'admin/notifications/ionic.html'
    form_class = NotificationsIonicForm

    def form_valid(self, form):
        data = form.cleaned_data
        payload = {key: data[key] for key in self.SUPPORTED_PAYLOAD_KEYS if data.get('key', NotificationsIonic)}
        filters = dict(
            bmi_from=data['bmi_from'],
            bmi_to=data['bmi_to']
        )

        success, errors, warnings = IonicApi().notify(data['title'], data['message'], filters=filters, **payload)
        return self.render_to_response(self.get_context_data(
            form=form,
            success=success.replace('\n', '<br>'),
            errors=errors,
            warnings=warnings
        ))
