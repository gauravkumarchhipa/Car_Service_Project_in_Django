from datetime import date
import datetime
from pyexpat import model
from telnetlib import STATUS
from unittest.util import _MAX_LENGTH
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customers(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    Gender = models.CharField(max_length=20, null=False)
    dob = models.DateField(null=True, blank=True)
    is_cust = models.BooleanField(default=True)


class Mechanic(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=False)
    skill = models.CharField(max_length=500, null=True)
    dob = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    salary = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)


class Add_Service(models.Model):
    service_name = models.CharField(max_length=20)
    service_charge = models.IntegerField(null=True, blank=True)
    service_desc = models.CharField(max_length=100)
    Petrol = models.IntegerField(null=True, blank=True)
    Diesel = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)


class Services_req(models.Model):
    userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Mechanic = models.ForeignKey(
        Mechanic, on_delete=models.CASCADE, default=1)
    car_company = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15)
    car_number = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    area = models.CharField(max_length=15)
    Mobile_Number = models.CharField(max_length=10)
    Service = models.ForeignKey(Add_Service, on_delete=models.CASCADE)
    Fuel = models.CharField(max_length=15, null=True)
    fuel_liter = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True)
    pd_date = models.DateField(blank=True, null=True)
    pd_time = models.CharField(max_length=15, null=True)
    pd_service = models.CharField(max_length=100, null=True)
    charge = models.CharField(max_length=15, null=True)
    Status = models.IntegerField(default=1, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # car_service_address = models.CharField(max_length=100, null=True)
    # pick_drop_address = models.CharField(max_length=100, null=True)


class request_assign(models.Model):
    Service = models.ForeignKey(Services_req, on_delete=models.CASCADE)
    userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    Status = models.IntegerField(default=1, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class add_car_service(models.Model):
    Srequest = models.ForeignKey(Services_req, on_delete=models.CASCADE)
    userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100, null=True)
    service_charge = models.CharField(max_length=100, null=True)


class service_payment(models.Model):
    Srequest = models.ForeignKey(Services_req, on_delete=models.CASCADE)
    userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    service_charge = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Membership(models.Model):
    userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    pay = models.IntegerField(default=1, blank=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)

class ContactUs(models.Model):
  userId = models.ForeignKey(Customers, on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  email=models.CharField(max_length=100,default="")
  number=models.CharField(max_length=15)
  msg=models.CharField(max_length=100)