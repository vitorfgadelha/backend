from rest_framework import serializers
from .models import Participant, Event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant 
        fields = ('bib', 'name', 'gender','dob', 'age', 'cpf', 'course', 'shirt', 'delivered', 'obs')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name','date','file')