from django.db import models
from django.forms import ModelForm
# Create your models here.

CHOICES = ( ('F', 'F'), ('NA', 'NA'), ('M', 'M'))
class Visa(models.Model):
    name = models.CharField(max_length=255)
    passport = models.CharField(max_length=10)
    dob = models.DateField()
    nationality = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now=True)


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = ['name', 'passport', 'dob', 'nationality', 'gender']
