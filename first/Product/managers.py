from django.db import models
from django.db.models.query import QuerySet

class ProductManager(models.Manager):

     def get_queryset(self): # This is used to custom our manager to get the field alphabetically
        return super().get_queryset().order_by('Product_name')
          
     def get_queryset(self):
        return super().get_queryset().order_by('Product_brand')
        
     def get_queryset(self):
        return super().get_queryset().filter(Product_price__gt=500)
     
     def get_queryset(self):
         return ProductQuerySet(self.model)
     
     def sorted(self): #Tis is custom method
         return super().get_queryset().order_by('Product_brand') #This will return everything aplhabetically A,b,c
     
     def sortByPrice(self):
         return super().get_queryset().order_by("Product_price")
    


class ProductQuerySet(models.QuerySet):   #This custom functions we will write all the logic in queryset Queryset is product object
        
        def getPawsIndia(self):
            return self.filter(Product_brand="PawPro")
            
        def get_queryset(self):
            return super().get_queryset().getPawsIndia()
        
        def toys(self):
            return self.filter(Product_name__icontains="toys")