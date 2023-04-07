from rest_framework import serializers
from .models import Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant 
        fields = ('bib', 'name', 'gender','dob', 'age', 'cpf', 'course', 'shirt', 'delivered', 'obs')