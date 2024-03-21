from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Product,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required(login_url="/login/"),name="dispatch")
class ProductView(ListView):
    model=Product
    template_name="Products.html"

class ProductDetailView(DetailView):
    model=Product
    template_name="Products_detail.html"
    context_object_name="P" 

def field_lookup(request):
 #products=Product.cm.all().filter(Q(Product_price__lt="1000")& Q(Product_name__icontains="")) AND Operator
 #products=Product.cm.all().filter(Q(id=5) | Q(id=6)) OR Operator 
 #products=Product.cm.all().filter(~Q(Product_brand="Hartz")) NOT Operator


 products=Product.cm.all() #Objects is our model manager by default our manager name is object
 #products=Product.objects.filter(Product_brand="Paws")
 #products=Product.objects.filter(Product_price__lt="500") #   we will use __ and lt to get the price which is lower than
 #products=Product.objects.filter(Product_price__lte="500") # we will use __lte to get the price which is more than or equal to 500
 #products=Product.objects.filter(Product_price__gt="700") #Gt is greater than 
 #products=Product.objects.filter(Product_price__gte="900") #GTE is greater than or equal
 #products=Product.objects.filter(Product_name__contains="Dog") # Case sensititve     
 #products=Product.objects.filter(Product_name__icontains="Dog") # This is not case sensitive we can write however we want to write   
 #products=Product.objects.filter(Product_name__startwith="D") # Which ever field name start with D it will show it in webpage
 #products=Product.objects.filter(Product_brand__startswith="P") # whatever brand name start with P will show in webpage   
 #products=Product.objects.filter(Product_name__istartswith="p") # Case insensititve     
#products=Product.objects.filter(Product_name__endswith="y") #It will show the name of field which ends with y   
#products=Product.objects.filter(Product_name__iendswith="Y") # It will show all the field name ending with Y or y 
#products=Product.objects.filter(id__in=[5,6,7]) # It will show the fields id whose are 5,6,7  



 return render(request,"Product_lookup.html",{"product":products})

class CategoryDetailView(DetailView):
   model=Category
   template_name="category.html"
   context_object_name="category"
   slug_field="slug"
   

