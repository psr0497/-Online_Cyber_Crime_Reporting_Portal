from django.shortcuts import render ,redirect
from . models import Gallery , Case ,Department
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.


def index(request):

    photos = Gallery.objects.all();
    print (photos);
    params ={'photo':photos};

    return render(request, 'cyber_cell/index.html',params);





def report(request):
    return render(request, 'cyber_cell/report_crime.html')


def complaint(request):
    status=Case.status;
    params={'status':status}
    return render(request, 'cyber_cell/complaint.html',params)


def submitcomplaint(request):

    if request.method=="POST":
       
        rname = request.POST.get('rname','')
        remail=request.POST.get('remail','')
        rphone=request.POST.get('rphone','')
        vname=request.POST.get('vname','')
        vemail=request.POST.get('vemail','')
        vphone=request.POST.get('vphone','')
        age=request.POST.get('age','')
        sex=request.POST.get('sex','')
        address=request.POST.get('address','')
        other=request.POST.get('other','')

        
        crimecases = Case( rname=rname, remail=remail, rphone=rphone, vname=vname, vemail=vemail, vphone=vphone, age=age, sex=sex, address=address, other=other)
        crimecases.save()
        
        messages.success(request,"Your Case is Registered Successfully")
        return redirect('index')
    return HttpResponse('404 Not Found')

def checkstatus(request):
    
    return render(request, 'cyber_cell/check_status.html')

def checkstatushandle(request):
    if request.method=='POST':
        vname=request.POST.get('vname','')

        myobject=Case.objects.filter(vname=vname).values('vname','id','vphone','age','sex','address','other','status')
        print(myobject)
        

        caseobject=list(myobject)
        victim=caseobject[0]
        victim_name=victim["vname"]
        cid=victim["id"]
        victim_phone=victim["vphone"]
        victim_age=victim["age"]
        victim_sex=victim["sex"]
        victim_address=victim["address"]
        victim_other=victim["other"]
        cstatus=victim["status"]
        params={'vname':victim_name,'rid':cid,'vphone':victim_phone,'vage':victim_age,'vsex':victim_sex,'vaddress':victim_address,'vother':victim_other,'cstatus':cstatus}
        return render(request,'cyber_cell/checkstats.html',params)
    
    return HttpResponse('404 Not Found')

def helpline(request):
    return render(request, 'cyber_cell/helpline.html')


def loginhandle(request):
    if request.method=="POST":
        
        
        name=request.POST['name']
        email=request.POST['email']
        login_pass=request.POST['login_pass']

        
        user = authenticate(request, username=name, password=login_pass)
        if user is not None:
            login(request, user)
            messages.success(request,"Welcome back")
            return redirect('index')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('index')
   
    return HttpResponse ('404 NOt Found')

def signuphandle(request):
    if request.method=="POST":

        name=request.POST.get('name','')
        designation=request.POST.get('designation','')
        region=request.POST.get('region','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        password=request.POST.get('pass','')
        confirm_pass=request.POST.get('confirm_pass','')
        key=request.POST.get('key','')

        d_key="9988"   
        

        if password != confirm_pass:
            messages.error(request,"Password Do Not Matched")
            return HttpResponse('404')

        if d_key!= key:
            messages.error(request,"Key Is Not Matched")
            return HttpResponse('Error 404')

        user = User.objects.create_user(name,email,password)
        user.save()

       

        duser=Department(designation=designation,region=region,phone=phone,user=user)
        duser.save()
        
        messages.success(request,"Your Account Is Created Successfully")
        return redirect('index')
    return HttpResponse("404 error")

def logouthandle(request):
    logout(request)
    messages.success(request,"Logout Successfuly")
    return redirect('index')

def contact(request):

    data=Department.objects.all()
    return render (request,'cyber_cell/contact.html',{'data':data})

def changes(request):
    if request.method=="POST":
        registration=request.POST.get('registration')
        status=request.POST.get('status')

        c=Case.objects.filter(id=registration).values('status')
        c.update(status=status)
       
        return redirect('checkstatus')

def updateStatus(request):
    return render(request,'cyber_cell/updateStatus.html')



def updateDetails(request):
    return render(request,'cyber_cell/updateDetails.html')

def updates(request):

    if request.method=="POST":
        registration=request.POST.get('Did')
        name=request.POST.get('name','')
        designation=request.POST.get('designation','')
        region=request.POST.get('region','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')

        C=User.objects.filter(username=name).values('email')
        C.update(email=email)
        U=Department.objects.filter(id=registration).values('designation','region','phone')
        U.update(designation=designation,region=region,phone=phone)
        return redirect('contact')

    return HttpResponse("404")