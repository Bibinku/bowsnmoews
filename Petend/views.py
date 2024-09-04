from django.shortcuts import render,redirect
from Petend.models import CategoryDB,BreadDB,FoodDB,AccessoriesDB,ServiceDB,Service1DB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Frontend.models import ContactDB,BookslotDB,FeedbackDB,OrderDb
from django.contrib import messages


# Create your views here.
def Indexpage(req):
    return render(req,"index.html")
def addcategory(req):
    return render(req,"addcategory.html")

def savecategory(req):
    if req.method=="POST":
        a=req.POST.get('cname')
        b=req.POST.get('cdescription')

        img=req.FILES['cimage']
        obj=CategoryDB(cname=a,cdescription=b,cimage=img,)
        obj.save()
        return redirect(Indexpage)

def displaycategory(req):
    data=CategoryDB.objects.all()
    return render(req,"displaycategory.html" , {'data':data})

def editcategory(req,Cid):
    data=CategoryDB.objects.get(id=Cid)
    return render(req,"editcategory.html",{'data':data})

def updatecategory(req,Cid):
    if req.method=="POST":
        a=req.POST.get('cname')


        b=req.POST.get('cdescription')

        try:
           img=req.FILES['cimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=Cid).cimage

    CategoryDB.objects.filter(id=Cid).update(cname=a,cdescription=b,cimage=file,)
    return redirect(displaycategory)


def deletecategory(req, Cid):
    data = CategoryDB.objects.filter(id=Cid)
    data.delete()
    messages.warning(req, "Category Deleted Successfully")
    return redirect(displaycategory)

def addbread(req):
    cat=CategoryDB.objects.all()
    return render(req,"addbread.html",{'cat':cat})

def savebread(req):
    if req.method=="POST":
        a=req.POST.get('category')
        b=req.POST.get('bname')
        c=req.POST.get('bage')
        d=req.POST.get('bgender')
        e=req.POST.get('bdescription')
        f=req.POST.get('bprice')
        g=req.POST.get('bvaccination')
        h=req.POST.get('bkci')

        img=req.FILES['bimage']
        obj=BreadDB(category=a,bname=b,bage=c,bgender=d,bimage=img,bdescription=e,bprice=f,bvaccination=g,bkci=h)
        obj.save()
        return redirect(Indexpage)

def displaybread(req):
    data=BreadDB.objects.all()
    return render(req,"displaybread.html" , {'data':data})

def editbread(req,Bid):
    data=BreadDB.objects.get(id=Bid)
    cat=CategoryDB.objects.all()
    return render(req,"editbread.html",{'data':data,'cat':cat})


def deletebread(req,Bid):
    data=BreadDB.objects.filter(id=Bid)
    data.delete()
    return redirect(displaybread)

def updatebread(req,Bid):
    if req.method=="POST":
        a = req.POST.get('category')
        b=req.POST.get('bname')
        c=req.POST.get('bage')
        d=req.POST.get('bgender')

        e=req.POST.get('bdescription')

        f=req.POST.get('bprice')
        g=req.POST.get('bvaccination')
        h=req.POST.get('bkci')



        try:
           img=req.FILES['bimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=BreadDB.objects.get(id=Bid).bimage

    BreadDB.objects.filter(id=Bid).update(category=a,bname=b,bage=c,bgender=d,bdescription=e,bprice=f,bvaccination=g,bkci=h,bimage=file)
    return redirect(Indexpage)


def adminlogin(req):
    return render(req,"adminlogin.html")

def admin(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a,password=b)
            if x is not None:
                login(request,x)
                request.session['username']=a
                request.session['password']=b
                messages.success(request,"Welcome..")
                return redirect(Indexpage)
            else:
                messages.warning(request,"Invaild username or password")
                return redirect(adminlogin)
        else:
            messages.warning(request,"Please check before enter ")
            return redirect(adminlogin)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"Logout Successfully")
    return redirect(adminlogin)


def displaycontact(req):
    data=ContactDB.objects.all()
    return render(req,"displaycontact.html",{'data':data})

def deletecontact(req,CONid):
    data=ContactDB.objects.filter(id=CONid)
    data.delete()
    return redirect(displaycontact)

def addfood(req):

    return render(req,"addfood.html")

def savefood(req):
    if req.method=="POST":
        a=req.POST.get('fname')
        b=req.POST.get('fdescription')
        c=req.POST.get('frate')
        img=req.FILES['fimage']
        obj=FoodDB(fname=a,fdescription=b,frate=c,fimage=img)
        obj.save()
        return redirect(Indexpage)

def displayfood(req):
    data=FoodDB.objects.all()
    return render(req,"displayfood.html" , {'data':data})

def editfood(req,Fid):
    data=FoodDB.objects.get(id=Fid)

    return render(req,"editfood.html",{'data':data,})


def deletefood(req,Fid):
    data=FoodDB.objects.filter(id=Fid)
    data.delete()
    return redirect(displayfood)

def updatefood(req,Fid):
    if req.method=="POST":
        a=req.POST.get('fname')
        b=req.POST.get('fdescription')
        c=req.POST.get('frate')

        try:
           img=req.FILES['fimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=Fid).fimage

    FoodDB.objects.filter(id=Fid).update(fname=a,fdescription=b,frate=c,fimage=file,)
    return redirect(displayfood)


def addaccessories(req):

    return render(req,"addaccessories.html")

def saveaccessories(req):
    if req.method=="POST":
        a=req.POST.get('aname')
        b=req.POST.get('adescription')
        c=req.POST.get('arate')
        img=req.FILES['aimage']
        obj=AccessoriesDB(aname=a,adescription=b,arate=c,aimage=img)
        obj.save()
        return redirect(Indexpage)

def displayaccessories(req):
    data=AccessoriesDB.objects.all()
    return render(req,"displayaccessories.html" , {'data':data})

def editaccessories(req,Aid):
    data=AccessoriesDB.objects.get(id=Aid)

    return render(req,"editaccessories.html",{'data':data,})


def deleteaccessories(req,Aid):
    data=AccessoriesDB.objects.filter(id=Aid)
    data.delete()
    return redirect(displayaccessories)

def updateaccessories(req,Aid):
    if req.method=="POST":
        a=req.POST.get('aname')
        b=req.POST.get('adescription')
        c=req.POST.get('arate')

        try:
           img=req.FILES['aimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=Aid).aimage

    AccessoriesDB.objects.filter(id=Aid).update(aname=a,adescription=b,arate=c,aimage=file,)
    return redirect(displayaccessories)


def addservice(req):
    return render(req,"addservice.html")

def saveservice(req):
    if req.method=="POST":
        a=req.POST.get('services')
        b=req.POST.get('sdescription')

        obj=ServiceDB(services=a,sdescription=b)
        obj.save()
        return redirect(Indexpage)

def displayservice(req):
    data=ServiceDB.objects.all()
    return render(req,"displayservice.html" , {'data':data})

def editservice(req,Sid):
    data=ServiceDB.objects.get(id=Sid)
    return render(req,"editservice.html",{'data':data})

def updateservice(req,Sid):
    if req.method=="POST":
        a=req.POST.get('services')
        b=req.POST.get('sdescription')

    ServiceDB.objects.filter(id=Sid).update(services=a,sdescription=b)
    return redirect(displayservice)


def deleteservice(req, Sid):
    data = ServiceDB.objects.filter(id=Sid)
    data.delete()
    messages.warning(req, "Category Deleted Successfully")
    return redirect(displayservice)


def addservice1(req):
    ser=ServiceDB.objects.all()
    return render(req,"addservice1.html",{'ser':ser})

def saveservice1(req):
    if req.method=="POST":
        a=req.POST.get('service1')
        g = req.POST.get('sdescription1')
        b=req.POST.get('feature1')
        c=req.POST.get('feature2')
        d=req.POST.get('feature3')
        e=req.POST.get('feature4')

        f=req.POST.get('sprice')

        img=req.FILES['simage']
        obj=Service1DB(service1=a,sprice=f,simage=img,feature1=b,feature2=c,feature3=d,feature4=e,sdescription1=g)
        obj.save()
        return redirect(Indexpage)

def displayservice1(req):
    data=Service1DB.objects.all()
    return render(req,"displayservice1.html" , {'data':data})

def editservice1(req,S1id):
    data=Service1DB.objects.get(id=S1id)
    ser=ServiceDB.objects.all()
    return render(req,"editservice1.html",{'data':data,'ser':ser})


def deleteservice1(req,S1id):
    data=Service1DB.objects.filter(id=S1id)
    data.delete()
    return redirect(displayservice1)

def updateservice1(req,S1id):
    if req.method=="POST":
        a = req.POST.get('service1')
        b = req.POST.get('feature1')
        c = req.POST.get('feature2')
        d = req.POST.get('feature3')
        e = req.POST.get('feature4')

        f = req.POST.get('sprice')
        g = req.POST.get('sdescription1')

        try:
           img=req.FILES['simage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Service1DB.objects.get(id=S1id).simage

    Service1DB.objects.filter(id=S1id).update(service1=a,feature1=b,feature2=c,feature3=d,feature4=e,sprice=f,sdescription1=g,simage=file,)
    return redirect(displayservice1)

def displaybookslot(req):
    book=BookslotDB.objects.all()
    return render(req,"displaybookslot.html",{'book':book})

def deletebookslot(req,Bookid):
    data=BookslotDB.objects.filter(id=Bookid)
    data.delete()
    return redirect(displaybookslot)


def displayfeedback(req):
    feed=FeedbackDB.objects.all()
    return render(req,"displayfeedback.html",{'feed':feed})

def deletefeedback(req,fid):
    data=FeedbackDB.objects.filter(id=fid)
    data.delete()
    return redirect(deletefeedback)






def displayorder(req):
    data=OrderDb.objects.all()
    return render(req,"displayorder.html" , {'data':data})

def deleteorder(req,Oid):
    data=OrderDb.objects.filter(id=Oid)
    data.delete()
    return redirect(displayorder)
