from django.db import models 

# class Item (models.Model):
#     item_name = models.CharField(max_length=50)
#     image = models.CharField(max_length=100)
#     ingredients  = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
   
class Blog(models.Model):
    title = models.CharField(max_length=400)
    image = models.CharField(max_length=100)
    content = models.CharField(max_length=1500) 
        
class Industry(models.Model):
    title = models.CharField(max_length=400)
    desc = models.CharField(max_length=400)
    content = models.CharField(max_length=1500) 
    image = models.CharField(max_length=100)

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)