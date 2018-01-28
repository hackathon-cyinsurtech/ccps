from django import forms
from django.forms import fields


class NotificationsIonicForm(forms.Form):
    title = fields.CharField(required=True, label='Notification title')
    message = fields.CharField(required=True, label='Notification message', widget=forms.Textarea)

    bmi_from = fields.IntegerField(required=False, label='BMI range from (optional)')
    bmi_to = fields.IntegerField(required=False, label='BMI range to (optional)')

    # ios_priority = fields.IntegerField(required=True, initial=10, help_text='')
    # android_priority = fields.ChoiceField(required=True, choices=[('high', 'high')], help_text='')
    # android_icon = fields.CharField(required=True, initial='notify', help_text='')
