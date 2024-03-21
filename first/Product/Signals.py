from django.contrib.auth.signals import *
#user_logged_in, user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *
from .models import Product

@receiver(user_logged_in,sender=User)
def log_In(sender,request,user,**kwargs):
    print("***************")
    print("Logged in successfully")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguement:",kwargs)
    print("***************")

@receiver(user_logged_out,sender=User)
def log_Out(sender,request,user,**kwargs):
    print("****")
    print("Logged out successfully")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print("Arguement:",kwargs)
    print("****")

@receiver(post_save,sender=Product)
def ProductCreateSignal(sender,instance,**kwargs):
        print("***********Product Created*************")
        print("****************************************")
        print("Sender:",sender)
        print("Instance:",instance)
        print("Arguements:",kwargs)
        print("****************************************")

@receiver(post_delete,sender=Product)
def ProductCreateSignal(sender,instance,**kwargs):
        print("***********Product Deleted*************")
        print("****************************************")
        print("Sender:",sender)
        print("Instance:",instance)
        print("Arguements:",kwargs)
        print("****************************************")
