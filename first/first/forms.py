from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        labels={"username":"Enter Username","email":"Email"}

        #fields="__all__" #To get all the variables that are in the admin (user)
        #form is a object
        #form.labels = Username,Firstname these are labels