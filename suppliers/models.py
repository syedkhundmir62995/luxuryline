# from typing_extensions import Required
from asyncio.windows_events import NULL
from datetime import date
from statistics import mode
from tkinter import Widget
from django.db import models
import uuid

from django.forms import DateInput, Textarea, widgets

# Create your models here.

class Material(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    mid = models.CharField(max_length=200,unique=True,blank=False)
    material = models.TextField(max_length=200,blank=False)
    quantity = models.IntegerField(blank=False)
    color = models.CharField(max_length=200,blank=False,default="None")
    date = models.DateField()
    scaleid = models.ForeignKey("Scale",on_delete=models.CASCADE)
    suupplierid = models.ForeignKey("Supplier",on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.material
        

class Scale(models.Model):
    scaleid = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    scale = models.CharField(max_length=100,blank=False,unique=True)

    def __str__(self):
        return self.scale

class Supplier(models.Model):
    supplierid = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    supplier_name = models.TextField(max_length=200,blank=False)
    supplier_address = models.TextField(max_length=300,blank=False)
    vat = models.CharField(max_length=200, blank= True, default=None)
    def __str__(self):
        return self.supplier_name



class MaterialTransaction(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    mid = models.CharField(max_length=200,blank=False)
    material = models.TextField(max_length=200,blank=False)
    quantity = models.IntegerField(blank=False)
    color = models.CharField(max_length=200,blank=False,default="None")
    date = models.DateField()
    scaleid = models.ForeignKey("Scale",on_delete=models.CASCADE)
    suupplierid = models.ForeignKey("Supplier",on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.material


class quotationitem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    item = models.CharField(default='None',unique=True ,max_length=300)
    # unit_price = models.FloatField()

    def __str__(self):
        return self.item


class quotationsize(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True)
    size = models.CharField(max_length=500, unique=True, default='None')

    def __str__(self):
        return self.size

# class quotationclient(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True)
#     clientname = models.CharField(max_length=500, default='None')
#     clientaddress = models.TextField(max_length=600, default='None')

#     def __str__(self):
#         return self.clientname


class quotationNumber(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quotation_number = models.CharField(default="0650",max_length=1000,unique=True)
    clientname = models.CharField(max_length=1000, default='Client Name')
    clientaddress = models.TextField(max_length=1000, default='Client Address')
    lastupdated = models.DateField(auto_now_add=True)
    #One quotation number is for one client(one to one relationship)
    def __str__(self):
        return self.quotation_number

class quotation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quotation_number = models.ForeignKey('quotationNumber', on_delete=models.CASCADE)
    item_name = models.ForeignKey('quotationitem',on_delete=models.CASCADE) 
    size = models.ForeignKey('quotationsize',on_delete=models.CASCADE)
    unit_price = models.FloatField()
    goods_description = models.TextField(max_length=1000)
    quantity = models.IntegerField(default=1)
    # client_name = models.ForeignKey('quotationclient', on_delete=models.CASCADE)
    date = models.DateField()
    total_price = models.FloatField()
    image = models.ImageField(upload_to = 'images')
    

    def __str__(self):
        return self.goods_description


class demo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # image = models.ImageField(upload_to= 'images/') 
    image = models.IntegerField()

    


class quotationAmount(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quotation_number = models.CharField(max_length=1000,unique=True)
    gross_amount = models.FloatField()
    vat = models.IntegerField()
    total_amount = models.FloatField()

    def __str__(self):
        return self.total_amount


