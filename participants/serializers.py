from rest_framework import serializers
from .models import Participant, Event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'id', 'chip', 'name', 'gender', 'dob', 'cpf', 'course','group', 'shirt', 'type', 'team', 'nation', 
            'medal_record', 'finisher', 'fisio', 'extra_shirt', 'phone', 'email', 'delivered', 'name_received', 
            'updated_at'
        )
        read_only_fields = ('updated_at',)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'file')
