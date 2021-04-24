from django.db import models

# Create your models here.


class Pharmacist(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(unique=True , max_length=20)
    fullName = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    contactNumber= models.CharField(max_length=12)
    aadharNumber=models.CharField(max_length = 16)

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







