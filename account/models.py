from django.db import models

# Create your models here.
class HomeSlider(models.Model):
   images      = models.ImageField(upload_to="home_slider")
   description = models.CharField(max_length = 150)
   img         = models.ImageField
  
   def __str__(self):
       return self.description
   

class ClientSlider(models.Model):
   name        = models.CharField(max_length=50)
   images      = models.ImageField(upload_to="client_slider")   
   description = models.CharField(max_length = 150)
   
   def __str__(self):
       return self.name

class Product(models.Model):
   description = models.CharField(max_length = 150)
   images      = models.ImageField(upload_to="product")   
   price       = models.IntegerField()
   name        = models.CharField(max_length = 50)
   
   def __str__(self):
       return self.name