from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ScrapeRun(models.Model):
    """This is the first model"""

    STATUS_CHOICES = (
        ("failed", "Failed"),
        ("in-progress", "In Progress"),
        ("complete", "Complete"),
    )

    target_url = models.URLField()
    result = models.CharField(max_length=30)
    result_json = models.JSONField()
    run_datetime = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="failed")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scrapes")

    class Meta:
        ordering = ("-run_datetime",)

    def __str__(self):
        return self.target_url + ", " + self.run_datetime

    def __unicode__(self):
        return self.target_url + ", " + self.run_datetime
