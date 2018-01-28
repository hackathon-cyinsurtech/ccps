from django.conf.urls import url

from . import views

ENDPOINT_NOTIFICATIONS_IONIC = '/notifications/'

urlpatterns = [
    url(r'' + ENDPOINT_NOTIFICATIONS_IONIC[1:] + '$', views.NotificationsIonic.as_view(), name='notifications_ionic'),
]
