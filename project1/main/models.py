from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length= 70)
    email = models.EmailField(max_length= 100)
    password = models.CharField(max_length= 100)

# class formdata(models.Model):
#     uname =models.CharField(max_length=20)
#     em = models.EmailField(max_length=20)
#     password = models.CharField( max_length=10)

    #form.py
    # "password":forms.PassordInput(render_value=True ,attrs={'class':'form-control'})