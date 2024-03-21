from django.db import models
from .managers import ProductManager
from autoslug import AutoSlugField




# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=13)
    slug=AutoSlugField(populate_from="category_name")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    Product_name=models.CharField(max_length=100,default="Product_name")
    Product_description=models.TextField(default="Product_description")
    Product_price=models.IntegerField(default=0)
    Product_brand=models.CharField(max_length=75,default="Paws")
    Product_picture=models.ImageField(upload_to="images/",default="")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)


    pm=models.Manager()  #This is used to change the name of the product manager by default it is object.
    cm=ProductManager()  #This is our custom manager 
    
    def __str__(self):
        return self.Product_name
    
    