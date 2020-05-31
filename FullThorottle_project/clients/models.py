from django.db import models

# Create your models here.
class Registration(models.Model):
    rid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    contactno=models.IntegerField(unique=True)
    password=models.CharField(max_length=20)


class Userlogin(models.Model):
    uid=models.AutoField(primary_key=True)
    uusername=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(null=True)