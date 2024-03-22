from rest_framework import serializers
from .models import Participant, Event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant 
        fields = ('bib','chip','name','gender','dob', 'cpf', 'course', 'shirt', 'delivered','type',
                  'obs','team','updated_at')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name','date','file')