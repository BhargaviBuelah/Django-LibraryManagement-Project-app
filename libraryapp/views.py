from django.shortcuts import render,redirect
from django.http import HttpResponse
from libraryapp.models import Book
from django.db.models import Q
from libraryapp.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError


#from todoapp.models import Product
# Create your views here.
def main(request):
    user_id=request.user.id
    #print("Hello")
    #return redirect('/index')
    if request.method=="POST":
        bname=request.POST['bname']
        bdesc=request.POST['bdesc']
        bauthor=request.POST['bauthor']
        copies=request.POST['copies']
        price=request.POST['bprice']
        cat=request.POST['cat']
        b1=Book(bname=bname,bdesc=bdesc,bauthor=bauthor,copies=copies,price=price,cat=cat,is_deleted="N",uid=user_id)
        #print(b1)
        b1.save()
        return redirect('/main')
    else:
        #show empty form
        #print("IN GET Section")
        #records=Book.objects.all()
        #records=Book.objects.filter(is_deleted="N")
        q1=Q(uid=user_id)
        q2=Q(is_deleted="N")
        records=Book.objects.filter(q1 & q2)
        print(records)
        content={}
        content['data']=records
        return render(request,'main.html',content)

def delete(request,rid):
    #Hard delete
    #x=Book.objects.get(id=rid)
    #x.delete()

    #soft delete
    x=Book.objects.filter(id=rid)
    x.update(is_deleted="Y")

    return redirect('/main')

def edit(request,rid):
    
    #str1="hello from edit function"
    #print(rid)
    if request.method=='POST':

        ubname=request.POST['bname']
        ubdesc=request.POST['bdesc']
        ubauthor=request.POST['bauthor']
        ucopies=request.POST['copies']
        uprice=request.POST['bprice']
        ucat=request.POST['cat']

        x=Book.objects.filter(id=rid)
        x.update(bname=ubname,bdesc=ubdesc,bauthor=ubauthor,copies=ucopies,price=uprice,cat=ucat)
        return redirect('/main')


    else:
        
        rec=Book.objects.get(id=rid)
        #print(rec)
        content={}
        content['data']=rec
        return render(request,'editbook.html',content)

#Sorting filter

def sort(request,sv):

    if sv=='ltoh':
      
        rec=Book.objects.filter(is_deleted="N").order_by('price')
           
    elif sv=='htol':
        
        rec=Book.objects.filter(is_deleted="N").order_by('-price')
         
    content={}
    content['data']=rec
    return render(request,'main.html',content)

#sorting with Name
def sortname(request,sn):
    if sn=='atoz':
        rec=Book.objects.filter(is_deleted="N").order_by('bauthor')
    elif sn=='ztoa':
        rec=Book.objects.filter(is_deleted="N").order_by('-bauthor')
    content={}
    content['data']=rec
    return render(request,'main.html',content)

#filter by catogery
def filter(request,vcat):
    #print(vcat)
    if vcat=="fict":
        f='F'
    elif vcat=="sci":
        f='S'
    elif vcat=="phil":
        f='Ph'
    elif vcat=="poetry":
        f='P'
    elif vcat=="drama":
        f='D'

  
    q1=Q(cat=f)
    q2=Q(is_deleted="N")
    rec=Book.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'main.html',content)


def register(request):
    
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password1']
        uemail=request.POST['email']
        fmdata=RegisterForm(request.POST)
        #print(fmdata)
        #print(uname)
        #print(upass)
        if fmdata.is_valid():
            fmdata.save()
            #return HttpResponse("User Registered successfully")
            #print(fmdata)
            subject = "Sending Password And Username"#            
            body = {
                'uname':fmdata.cleaned_data['username'],
                'upass':fmdata.cleaned_data['password1']
            }
            
            message = '\n'.join(body.values())
            sender = fmdata.cleaned_data['email']
            recipient = ['bhargavi.django@gmail.com']
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Your respoce has been submited successfully")#
            
            return redirect('/login')
    
        else:
            
            return HttpResponse("fail to create user")
    else:
        #rfm=UserCreationForm()
        rfm=RegisterForm()
        return render(request,'register.html',{'rform':rfm})
    context = {             #
        'fmdata':fmdata,
    }

def user_login(request):

    if request.method=="POST":
        lfm=AuthenticationForm(request=request,data=request.POST)
        #print(lfm)
        if lfm.is_valid():
            uname=lfm.cleaned_data['username']
            upass=lfm.cleaned_data['password']
            #print(uname)
            #print(upass)
            #select * from auth_user where username=name and password=pass
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u) #It start session for that logged in user and store id of that user in the session
                return redirect('/main')
        else:
                return HttpResponse("Invalid username or password")
    else:
        lfm=AuthenticationForm()
        print("In user_login else part")
        return render(request,'login.html',{'lform':lfm})
   

def user_logout(request):

    logout(request)#This functionality destroy session
    return redirect('/login')




