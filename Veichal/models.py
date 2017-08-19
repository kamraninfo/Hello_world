from django.db import models
from django.urls import reverse


class Car(models.Model):
    carid=models.AutoField(primary_key=True)
    CarModel=models.CharField(max_length=50)
    year=models.CharField(max_length=4)
    color=models.CharField(max_length=20)
    Price=models.CharField(max_length=8)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('country:car-list')
class Meta:
        managed=True

class Country(models.Model):
    countryid=models.AutoField(primary_key=True)
    countryname=models.CharField(max_length=200)
    carid=models.ForeignKey('Car',models.DO_NOTHING,db_column='carid')

class Meta:
    managed=True





