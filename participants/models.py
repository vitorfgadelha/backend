from django.db import models

class Participant(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('MX', 'Mixed')
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

    bib = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField('Name', max_length=240, null=True)
    gender = models.CharField(max_length=2, choices=GENDER,default=None,null=True)
    dob = models.DateField('DoB',null=True)
    cpf = models.CharField('CPF',max_length=15,null=True)
    course = models.CharField('Course', max_length=50,null=True)
    shirt = models.CharField('Shirt', choices=SHIRT, max_length=3,null=True)
    delivered = models.BooleanField('Delivered', default=False)
    obs = models.CharField('Obs', max_length=240, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Name', max_length=200)
    date = models.DateField('Date')
    file = models.FileField('File',upload_to ='events/')