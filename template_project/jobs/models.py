from django.db import models

# Create your models here.
from django.utils import timezone


class Job(models.Model):
    name = models.CharField(max_length=255)
    # FIXME Use choices for status
    status = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    completed = models.DateTimeField(null=True, blank=True)
    celery_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name
