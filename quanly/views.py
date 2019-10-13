from django.shortcuts import render, redirect, render_to_response
from django.http import Http404,HttpResponse
from quanly import models

def Base_login(request):
    #check account
    error={}
    data={}
    if request.method=='POST':
        data['username'] = request.POST.get('Username')
        data['password'] = request.POST.get('Password')
    return render(request,'login.html')
def Base_register(request):
    error = {}
    data = {}
    if request.method == 'POST':
        data['username'] = request.POST.get('Username') #
        data['password'] = request.POST.get('password')
        data['mail']=request.POST.get('email')
        count = models.Account.objects.filter(user= data['username']).count()
        if count > 0:
            error['exist'] = "This account already exist!"
        else:
            ds = models.Account(user= data['username'], password= data['password'], mail = data['mail'])
            ds.save()
            return redirect('mailconfirm')
    return render(request,'register.html', {'error': error})
def Base_mailconfirm(request):
	return render(request,'mailconfirm.html')
def Base_home(request):
    return render(request,'home.html')
