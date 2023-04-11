from rest_framework import viewsets, filters

from .models import Participant, Event
from .serializers import ParticipantSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from django.core.paginator import Paginator



import json
from openpyxl import load_workbook
import datetime 


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('bib')
    serializer_class = ParticipantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','cpf']

    @action(detail=False)
    def count_delivered(*args, **kwargs):
        participant_count = Participant.objects.filter(delivered = True).count()
        return Response(str(participant_count))
    
    @action(detail=False)
    def count_not_delivered(*args, **kwargs):
        participant_count = Participant.objects.filter(delivered = False).count()
        return Response(str(participant_count))

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False)
    def create_participants(*args, **kwargs):
        workbook = load_workbook(filename="media/Corrida.xlsx")
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, min_col=1,max_col=8,values_only=True):
            participant = Participant(bib=row[0],
                                      name=row[1],
                                      gender=row[2],
                                      dob=row[3],
                                      cpf=row[5],
                                      course=row[6],
                                      shirt=row[7],
                                      delivered='False')
            participant.save()
        return Response('Success, all participants added.')