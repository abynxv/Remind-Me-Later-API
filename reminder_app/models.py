from django.db import models
from django.contrib.auth.models import User


class Reminder(models.Model):
    REMINDER_CHOICES = (
        ('email', 'Email'),
        ('sms', 'SMS')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_CHOICES)