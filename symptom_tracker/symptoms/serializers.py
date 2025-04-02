from rest_framework import serializers
from .models import Symptom

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'user', 'date_logged', 'symptom_type', 'severity']
        read_only_fields = ['id', 'user', 'date_logged']
