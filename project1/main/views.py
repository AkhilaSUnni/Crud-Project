
from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import  studentregistration
# Create your views here.

#This function will add new item and show all items


def add_show(request):
    if request.method =='POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = user(name=nm, email=em, password = pw)
         reg.save()
         fm = studentregistration() 
    else:
        fm = studentregistration()
    stud = user.objects.all()
    return render(request,'addandshow.html',{'form':fm ,'stu':stud})

# def add_show(request):
#     if request.method == 'POST':
#        d ={
#            'stu':user.objects.all()
#        }
#        name = request.POST.get('user_name')
#        email = request.POST.get('user_email')
#        password = request.POST.get('password')

#        ob =formdata(uname=name,em=email,password=password)
#        ob.save()
#        return render(request,'addandshow.html')
#     return render(request,'addandshow.html',d)


#this function will update/edit
def update_data(request,id):
   if request.method == 'POST':
     pi = user.objects.get(pk=id)
     fm =studentregistration(request.POST.get(instance=pi)) 
     if fm.is_valid():
       fm.save() 
   else:
       pi = user.objects.get(pk=id)
       fm =studentregistration(instance=pi)  
   return render(request,'updatestudent.html', {'form':fm})
 
#this function will delete
def delete_data(request,id):
     if request.method == 'POST':
         pi = user.objects.get(pk=id)
         pi.delete()
         return HttpResponseRedirect('/')