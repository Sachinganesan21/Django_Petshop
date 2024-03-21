from django.shortcuts import render,HttpResponse
from django.views import View



# Create your views here.

def home(request):
    return HttpResponse("First view")

def firstpage(request):
    return HttpResponse("<h1>First Page</h1>")

def about(request):
    return HttpResponse("My name is Sachin Ganesan. I am 26 years old I stay in Kalina Santacruz(east) Mumbai 40092")

def contact(request):
    return HttpResponse("Contact no: 8452024969")
    
def contact(request):
    return HttpResponse("Mail id: sachinbalganeshan174@gmail.com")
    
def users(request):
    student={
        "id":100,
        "Name":"Karim",
        "age":30
    }
    return render(request,"index.html",student)

def student(request):
    Student={
        "ID":666,
        "Age":66
    } 
    return render(request,"itvandheri.html",Student)

def register(request):
    return render(request,"register.html")

def submit(request):
    if request.method=="POST":
        return render(request,"submit.html")
    if request.method=="GET":
        return render(request,"register.html")
    
#Class based view
class firstView(View):
    def get(self,request):
        return HttpResponse("Class Based View -GET")
    
class secondView(View):
    name="Sai"
    def get(self,request):
        return render(request,"detail.html",{"name":self.name})
    
