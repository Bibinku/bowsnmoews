from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    cname= models.CharField(max_length=100, null=True, blank=True)
    cdescription= models.CharField(max_length=500, null=True, blank=True)
    cimage = models.ImageField(upload_to="Category image", null=True, blank=True)

class BreadDB(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    bname = models.CharField(max_length=100, null=True, blank=True)

    bgender = models.CharField(max_length=500, null=True, blank=True)
    bdescription = models.CharField(max_length=500, null=True, blank=True)
    bimage = models.ImageField(upload_to="Product_images", null=True, blank=True)
    bage=models.CharField(max_length=50,null=True,blank=True)
    bprice=models.IntegerField(null=True,blank=True)
    bvaccination= models.CharField(max_length=100, null=True, blank=True)
    bkci= models.CharField(max_length=100, null=True, blank=True)



class FoodDB(models.Model):
    fname=models.CharField(max_length=100,null=True,blank=True)
    fdescription=models.CharField(max_length=500,null=True,blank=True)
    frate=models.IntegerField(null=True,blank=True)
    fimage = models.ImageField(upload_to="Food_images", null=True, blank=True)

class AccessoriesDB(models.Model):
    aname=models.CharField(max_length=100,null=True,blank=True)
    adescription=models.CharField(max_length=500,null=True,blank=True)
    arate=models.IntegerField(null=True,blank=True)
    aimage = models.ImageField(upload_to="Accessories_images", null=True, blank=True)

class ServiceDB(models.Model):
    services=models.CharField(max_length=100,null=True,blank=True)
    sdescription = models.CharField(max_length=500, null=True, blank=True)


class Service1DB(models.Model):
    service1=models.CharField(max_length=100,null=True,blank=True)
    sdescription1 = models.CharField(max_length=500, null=True, blank=True)


    feature1=models.CharField(max_length=100,null=True,blank=True)
    feature2=models.CharField(max_length=100,null=True,blank=True)
    feature3=models.CharField(max_length=100,null=True,blank=True)
    feature4=models.CharField(max_length=100,null=True,blank=True)

    sprice = models.IntegerField(null=True, blank=True)
    simage = models.ImageField(upload_to="Service_images", null=True, blank=True)


class ReplayDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    replay1=models.CharField(max_length=100,null=True,blank=True)
    replay2=models.CharField(max_length=100,null=True,blank=True)
