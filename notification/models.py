from django.db import models


class NotificationType(models.Model):
    permission = models.ManyToManyField('notification.NotificationPermissions')


class NotificationPermissions(models.Model):
    permission = models.SlugField(max_length=150)
    description = models.CharField(max_length=250)


class Notification(models.Model):
    ...
