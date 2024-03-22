from rest_framework import viewsets, filters

from .models import Participant, Event
from .serializers import ParticipantSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from django.core.paginator import Paginator

import json
from openpyxl import load_workbook, Workbook
import datetime 

import time

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
    
    @action(detail=False)
    def generate_report(*args, **kwargs):
        book = Workbook()
        sheet = book.active
        participants = Participant.objects.all().order_by('bib')
        sheet['A1'] = 'BIB'
        sheet['B1'] = 'CHIP'
        sheet['C1'] = 'NOME'
        sheet['D1'] = 'SEXO'
        sheet['E1'] = 'DOB'
        sheet['F1'] = 'CPF'
        sheet['G1'] = 'PROVA'
        sheet['H1'] = 'CAMISA'
        sheet['I1'] = 'TIPO'
        sheet['J1'] = 'EQUIPE'
        sheet['K1'] = 'ENTREGUE'
        sheet['L1'] = 'ATUALIZADO'
        sheet['M1'] = 'OBS'
        i = 2
        for participant in participants:
            sheet['A' + str(i)] = participant.bib
            sheet['B' + str(i)] = participant.chip
            sheet['C' + str(i)] = participant.name
            sheet['D' + str(i)] = participant.gender
            sheet['E' + str(i)] = participant.dob
            sheet['F' + str(i)] = participant.cpf
            sheet['G' + str(i)] = participant.course
            sheet['H' + str(i)] = participant.shirt
            sheet['I' + str(i)] = participant.type
            sheet['J' + str(i)] = participant.team
            sheet['K' + str(i)] = participant.delivered
            sheet['L' + str(i)] = str(participant.updated_at)
            sheet['M' + str(i)] = participant.obs
            i = i + 1
        book.save(filename="media/Report.xlsx")
        return Response('Success, report generated successfully.')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    @action(detail=False)
    def create_participants(*args, **kwargs):
        start_time = time.time()
        workbook = load_workbook(filename="media/Entrega_Kits.xlsx")
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1,max_col=sheet.max_column,values_only=True):
            if row[0] != '':
                participant = Participant(bib=row[0],
                                          chip=row[1],
                                          name=row[2],
                                          gender=row[3],
                                          dob=row[4],
                                          cpf=str(row[5]).zfill(11),
                                          course=row[6],
                                          shirt=row[7],
                                          type=row[8],
                                          team=row[9],
                                          delivered='False')
                participant.save()
        print("--- %s seconds ---" % (time.time() - start_time))
        return Response('Success, all participants added.')