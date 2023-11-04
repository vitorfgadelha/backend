from rest_framework import viewsets, filters

from .models import Participant, Event
from .serializers import ParticipantSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from django.core.paginator import Paginator

from openpyxl import load_workbook, Workbook


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
        sheet['B1'] = 'NAME'
        sheet['C1'] = 'SEXO'
        sheet['D1'] = 'DOB'
        sheet['E1'] = 'CPF'
        sheet['F1'] = 'PROVA'
        sheet['G1'] = 'CAMISA'
        sheet['H1'] = 'ENTREGUE'
        sheet['I1'] = 'ATUALIZADO'
        i = 2
        for participant in participants:
            sheet['A' + str(i)] = participant.bib
            sheet['B' + str(i)] = participant.name
            sheet['C' + str(i)] = participant.gender
            sheet['D' + str(i)] = participant.dob
            sheet['E' + str(i)] = participant.cpf
            sheet['F' + str(i)] = participant.course
            sheet['G' + str(i)] = participant.shirt
            sheet['H' + str(i)] = participant.delivered
            sheet['I' + str(i)] = str(participant.updated_at)
            i = i + 1
        book.save(filename="media/Report.xlsx")
        return Response('Success, report generated successfully.')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    @action(detail=False)
    def create_participants(*args, **kwargs):
        workbook = load_workbook(filename="media/Corrida.xlsx")
        sheet = workbook.active
        print(sheet.max_row)
        for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1,max_col=8,values_only=True):
            if row[0] != '':
                participant = Participant(bib=row[0],
                                      name=row[1],
                                      gender=row[2],
                                      dob=row[3],
                                      cpf=str(row[4]).zfill(11),
                                      course=row[5],
                                      shirt=row[6],
                                      delivered='False')
                participant.save()
        return Response('Success, all participants added.')