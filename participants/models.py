from django.db import models

class Participant(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    SHIRT = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
        ('8','8'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('PP','PP'),
        ('P','P'),
        ('M','M'),
        ('G','G'),
        ('GG','GG'),
        ('XG','XG'),
    )

    bib = models.IntegerField(unique=True)
    name = models.CharField('Name', max_length=240)
    gender = models.CharField(max_length=1, choices=GENDER,default=None)
    dob = models.DateField('DoB')
    age = models.IntegerField('Age')
    cpf = models.CharField('CPF',max_length=15)
    course = models.CharField('Course', max_length=50)
    shirt = models.CharField('Shirt', choices=SHIRT, max_length=3)
    delivered = models.BooleanField('Delivered', default=False)
    obs = models.CharField('Obs', max_length=240, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Name', max_length=200)
    date = models.DateField('Date')
    file = models.FileField('File',upload_to ='events/')