from datetime import datetime, timezone  # Corrigindo a importação de datetime e timezone
from django.db import models

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

SHIRT_SIZES = [
    ('BL PP', 'BL PP'),
    ('BL P', 'BL P'),
    ('BL M', 'BL M'),
    ('BL G', 'BL G'),
    ('PP', 'PP'),
    ('P', 'P'),
    ('M', 'M'),
    ('G', 'G'),
    ('GG', 'GG'),
    ('XG', 'XG'),
]

GROUP_CHOICES = [
    ('CADEIRANTE', 'CADEIRANTE'),
    ('VISUAL', 'VISUAL'),
    ('ELITE', 'ELITE'),
    ('PUBLICO GERAL', 'PUBLICO GERAL'),
    ('PCD', 'PCD')
]

class Participant(models.Model):
    id = models.AutoField('ID', unique=True, primary_key=True)
    chip = models.IntegerField('Chip', null=True, blank=True)
    name = models.CharField('Name', max_length=75, null=True, blank=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField('Date of Birth', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=15, null=True, blank=True)
    course = models.CharField('Course', max_length=10, null=True, blank=True)
    group = models.CharField('Group', max_length=13, choices=GROUP_CHOICES, null=True, blank=True)
    shirt = models.CharField('Shirt', max_length=5, choices=SHIRT_SIZES, null=True, blank=True)
    type = models.CharField('Type', max_length=20, null=True, blank=True)
    team = models.CharField('Team', max_length=50, null=True, blank=True)
    nation = models.CharField('Nation', max_length=30, null=True, blank=True)
    medal_record = models.BooleanField('Medal Record', default=False)
    finisher = models.CharField('Finisher', max_length=5, choices=SHIRT_SIZES, null=True, blank=True)
    fisio = models.BooleanField('Fisio', default=False, null=True, blank=True)
    extra_shirt = models.CharField('Extra Shirt', max_length=5, choices=SHIRT_SIZES, null=True, blank=True)
    phone = models.CharField('Phone', max_length=15, null=True, blank=True)
    email = models.EmailField('Email', max_length=254, null=True, blank=True)
    delivered = models.BooleanField('Delivered', default=False)
    name_received = models.CharField('Name Received', max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField('Updated At', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = Participant.objects.get(pk=self.pk)
            if old_instance.delivered != self.delivered:
                self.updated_at = datetime.now(timezone.utc)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "Unnamed Participant"

class Event(models.Model):
    name = models.CharField('Name', max_length=200)
    date = models.DateField('Date')
    file = models.FileField('File', upload_to='events/')

    def __str__(self):
        return self.name
