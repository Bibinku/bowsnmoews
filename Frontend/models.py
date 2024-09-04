from django.db import models

# Create your models here.
class ContactDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    message=models.CharField(max_length=500,null=True,blank=True)

class Registerdb(models.Model):
    USERNAME=models.CharField(max_length=100,null=True,blank=True)
    EMAIL=models.EmailField(max_length=100,null=True,blank=True)
    PASSWORD1=models.CharField(max_length=100,null=True,blank=True)
    PASSWORD2=models.CharField(max_length=100,null=True,blank=True)

class BookslotDB(models.Model):
    Bservices=models.CharField(max_length=100,null=True,blank=True)
    Bname=models.CharField(max_length=100,null=True,blank=True)
    Bnumber=models.IntegerField(null=True,blank=True)
    Bbread=models.CharField(max_length=100,null=True,blank=True)
    Bage=models.CharField(max_length=100,null=True,blank=True)
    Bsex=models.CharField(max_length=100,null=True,blank=True)
    Bdate=models.CharField(max_length=100,null=True,blank=True)
    Btime=models.CharField(max_length=100,null=True,blank=True)
    Bmessage=models.CharField(max_length=1000,null=True,blank=True)



class CartDb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)


class OrderDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)

    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)

class FeedbackDB(models.Model):
    Fname=models.CharField(max_length=100,null=True,blank=True)
    Fphone=models.IntegerField(null=True,blank=True)
    Fmessage=models.CharField(max_length=500,null=True,blank=True)
