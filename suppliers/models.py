# from typing_extensions import Required
from asyncio.windows_events import NULL
from statistics import mode
from django.db import models
import uuid

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
