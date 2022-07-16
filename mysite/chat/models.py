from django.db import models
from simple_history.models import HistoricalRecords


class Log(models.Model):
    topic = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.topic} - {self.created}'
