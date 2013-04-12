from django.db import models
from django.forms import ModelForm, Textarea
from django import forms

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phno = models.BigIntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    #password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name


class Advertisement(models.Model):
    ad_by = models.ForeignKey(Customer)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __unicode__(self):
        return self.name


class Bid(models.Model):

    cust_id = models.ForeignKey(Customer)
    ad_id = models.ForeignKey(Advertisement)
    price = models.IntegerField()


class AdvertiseForm(ModelForm):
    description = forms.CharField(widget=Textarea)

    class Meta:
        model = Advertisement
        exclude = ('ad_by',)
