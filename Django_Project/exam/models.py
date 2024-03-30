from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class Meta:
        db_table="Signupexam" #To show the table name to the user

class Login(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    class Meta:
        db_table="Loginexam"