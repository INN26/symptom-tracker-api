from django.db import models
from django.conf import settings

class Symptom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='symptoms')
    date_logged = models.DateTimeField(auto_now_add=True)
    symptom_type = models.CharField(max_length=100)
    severity = models.IntegerField()

    def __str__(self):
        return f"{self.symptom_type} ({self.severity}) on {self.date_logged.date()}"
