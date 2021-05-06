from django.db import models
from datetime import datetime
# Create your models here.


class Pharmacist(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(unique=True , max_length=20)
    fullName = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    contactNumber= models.CharField(max_length=12)
    aadharNumber=models.CharField(max_length = 16, unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    contactNumber= models.CharField(max_length=12 , primary_key = True)
    email = models.EmailField(unique = True)
    fullName = models.CharField(max_length=255)
    address = models.CharField(max_length = 255)
    dob = models.DateField()
    aadharNumber=models.CharField(max_length = 16)


    def __str__(self):
        return self.fullName + " " + self.contactNumber


class Doctor(models.Model):
    docId= models.AutoField(primary_key = True)
    doctorName = models.CharField(max_length = 255 , unique=True)
    hospitalName = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)

    def __str__(self):
        return self.doctorName + " " + self.hospitalName




class Medicine(models.Model):
    medicineId= models.AutoField(primary_key = True)
    medicineName = models.CharField(max_length = 255 , unique=True)
    schedule = models.CharField(max_length=13, choices=(("1","1"),("2","2"),("3","3")), default="1")
    price = models.FloatField()


class Billing(models.Model):
    billId = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'billing')
    pharmacist = models.ForeignKey(Pharmacist, on_delete = models.CASCADE, related_name = 'billing')
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name = 'billing', null=True, blank=True)
    billAmount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE, related_name = 'entry')
    bill = models.ForeignKey(Billing, on_delete = models.CASCADE, related_name = 'entry')
    quantity = models.IntegerField()
    price = models.FloatField()