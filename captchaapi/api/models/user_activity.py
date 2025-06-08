from django.db import models
from django.contrib.postgres.fields import JSONField  # if using Postgres


class Mode(models.IntegerChoices):
    BOT = 0, 'BOT'
    USER = 1, 'USER',
    NOT_LABELED = 2, 'NOT_LABELED'


class UserActivity(models.Model):
    mouse_movements = models.JSONField(default=list)
    scroll_events = models.JSONField(default=list)
    typing_patterns = models.JSONField(default=list)
    click_patterns = models.JSONField(default=list)
    touch_interactions = models.JSONField(default=list)

    user_agent = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_id = models.CharField(max_length=255)
    response_time = models.IntegerField(help_text="Response time in milliseconds")
    navigation_start = models.BigIntegerField(help_text="Timestamp of navigation start (ms since epoch)")
    mode = models.PositiveIntegerField(default=Mode.NOT_LABELED, choices=Mode.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UserActivity {self.id} - Device {self.device_id}"