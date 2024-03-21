from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,HttpResponse
from Product.models import Product
from .models import Cart,CartItem         
          

# Create your views here.

def add_to_cart(request,ProductId):
    #logic for adding cart

    product=get_object_or_404(Product,id=ProductId)
    #print(product.Product_name)


    #Fetching current user
    currentUser=request.user

    cart,created=Cart.objects.get_or_create(user=currentUser)

    print(created)

    item,item_created=CartItem.objects.get_or_create(cart=cart,Products=product)

    quantity=request.GET.get("quantity")

    if not item_created:
        item.Quantity+=int(quantity)
        
    else:
        item.Quantity=1

    item.save()

    return HttpResponseRedirect("/Pro/productlookup/")

#===================================================
#            View Cart
#==================================================

def view_cart(request):
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=cart.cartitem_set.all()
    print(cartItems)
    finalAmount=0

    for item in cartItems:
        finalAmount+=item.Quantity*item.Products.Product_price

    return render(request,"cart.html",{"items":cartItems,"finalAmount":finalAmount})

#--------------------------------------------
#           UPDATE CART
#--------------------------------------------

def update_cart(request,cartItemId):

   cartItem=get_object_or_404(CartItem,pk=cartItemId) 
   Quantity=request.GET.get("quantity")
   print(Quantity)
   cartItem.Quantity=int(Quantity)
   print(cartItem.Quantity)
   cartItem.save()


   return HttpResponseRedirect("/cart/")
#===================================================
#            Delete Cart Item
#==================================================

def delete_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    cartItem.delete()
    return HttpResponseRedirect("/cart/")

#===================================================
#            CHECKOUT
#===================================================

from .forms import OrderForm
from .models import Order,OrderItem
import uuid


def check_out(request):

    currentUser=request.user

    initial={
        "user":currentUser,
        "first_name":currentUser,
        "last_name":currentUser.last_name,
        "email":currentUser.email
        
    
    }
    print(initial['user'])
    form=OrderForm(initial=initial)

    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=cart.cartitem_set.all()
    print(cartItems)
    finalAmount=0

    for item in cartItems:
        finalAmount+=item.Quantity*item.Products.Product_price

    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            user=request.user
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phoneno=form.cleaned_data['phoneno']

            orderId=str(uuid.uuid4())   

            order=Order.objects.create(user=user,
                                 first_name=first_name,
                                 last_name=last_name,
                                 address=address,
                                 email=email,
                                 city=city,
                                 state=state,
                                 pincode=pincode,
                                 phoneno=phoneno,
                                 order_id=orderId[:8]
                                 )
            
            for item in cartItems:
                OrderItem.objects.create(
                    order=order,
                    Products=item.Products,
                    Quantity=item.Quantity,
                    Total=item.Quantity*item.Products.Product_price
                )




        return HttpResponseRedirect("/payment/"+orderId[:8])

    return render(request,"checkout.html",{"form":form,"items":cartItems,"finalAmount":finalAmount})

#===================================================
#            Make Payment
#===================================================

import razorpay
import setuptools

def make_payment(request,orderId):
    #print(orderId)
    order=Order.objects.get(pk=orderId)
    orderItems=order.orderitem_set.all()
    amount=0
    for item in orderItems:
        amount+=item.Total

    print(amount)
    import razorpay
    client = razorpay.Client(auth=("rzp_test_arPMbeh4QMV58V", "v9O0m9tx08x2pxSfQoy0xKOe"))
    data = { "amount": amount*100, "currency": "INR", "receipt": orderId ,"payment_capture":1 }
    payment = client.order.create(data=data)


    return render(request,"payment.html",{"payment":payment})


#===================================================
#            Success Page
#===================================================

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string



@csrf_exempt
def success(request,orderId):
    if request.method=="POST":
            client = razorpay.Client(auth=("rzp_test_arPMbeh4QMV58V", "v9O0m9tx08x2pxSfQoy0xKOe"))
            check=client.utility.verify_payment_signature({
                    'razorpay_order_id': request.POST.get("razorpay_order_id"),
                    'razorpay_payment_id': request.POST.get("razorpay_payment_id"),
                    'razorpay_signature': request.POST.get("razorpay_signature")
                 })
            if check:
                order=Order.objects.get(pk=orderId)
                order.paid=True
                order.save()
                cart=Cart.objects.get(user=request.user)
                OrderItem=order.orderitem_set.all()
                send_mail(
                    "Order Placed", #SUBJECT
                    "", #Message
                    settings.EMAIL_HOST_USER,
                    ["nihalruke1232001@gmail.com","jari.jafri21@gmail.com"],
                    fail_silently=False,
                    html_message=render_to_string("email.html",{"items":OrderItem})
                )
                cart.delete()
                

                return render(request,"success.html",{})
    
                



