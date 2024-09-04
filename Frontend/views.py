from django.shortcuts import render, redirect, get_object_or_404
from Petend.models import BreadDB,AccessoriesDB,FoodDB,Service1DB
from Frontend.models import ContactDB,Registerdb,BookslotDB,CartDb,OrderDb,FeedbackDB
from django.contrib import messages
import razorpay
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from django.core.exceptions import ValidationError
import datetime
from django.core.mail import send_mail, BadHeaderError
from PetCare import settings


# Create your views here.

def homepage(req):

    data=Service1DB.objects.all()
    feed=FeedbackDB.objects.all()
    ser=Service1DB.objects.all()




    return render(req,"home.html",{'data':data,'feed':feed,'ser':ser})

def aboutpage(req):
    feed = FeedbackDB.objects.all()
    return  render(req,"about.html",{'feed':feed})


def servicepage(req):
    return  render(req,"service.html")
def contactpage(req):
    return  render(req,"contact.html")

def breadpage(req):
    bre=BreadDB.objects.all()
    return  render(req,"bread.html",{'bre':bre})

def savecontact(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('phone')
        d=req.POST.get('subject')
        f=req.POST.get('message')
        obj=ContactDB(name=a,email=b,phone=c,subject=d,message=f)
        obj.save()
        messages.success(req,"Thanks for Contacting Us!")
        return redirect(contactpage)

def accessoriespage(req):
    Acc=AccessoriesDB.objects.all()
    return render(req,"accessories.html",{'Acc':Acc})

def foodpage(req):
    fd=FoodDB.objects.all()
    return render(req,"food.html", {'fd':fd})

def servicepage(req):
    ser=Service1DB.objects.all()
    return render(req,"service.html",{'ser':ser})




def signuppage(req):
    return  render(req,"signup.html")

def save_user(req):
    if req.method=="POST":
        a=req.POST.get('USERNAME')
        b=req.POST.get('EMAIL')
        c=req.POST.get('PASSWORD1')
        d=req.POST.get('PASSWORD2')

        obj=Registerdb(USERNAME=a,EMAIL=b,PASSWORD1=c,PASSWORD2=d)
        if Registerdb.objects.filter(USERNAME=a).exists():
            messages.warning(req,"User already exists...")
        elif Registerdb.objects.filter(EMAIL=b).exists():
            messages.warning(req,"Email Already exists....")
        else:
            obj.save()
            messages.success(req,"User added successfully....")

            user_email = b
            # Send Login confirmation email
            send_login_confirmation_email(user_email)
        return redirect(signinpage)

def send_login_confirmation_email(user_email):
    subject = 'Login Confirmation'
    message = f'Welcome to Bows N Moews '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    try:
        send_mail(subject, message, email_from, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # Log the error or handle it as necessary
        return HttpResponse(f'Error sending email: {e}')


def userlogin(req):
    if req.method=="POST":
        un=req.POST.get('yourname')
        pwd=req.POST.get('yourpassword')


        if Registerdb.objects.filter(USERNAME=un,PASSWORD1=pwd,).exists():
            req.session['USERNAME']=un
            req.session['PASSWORD1']=pwd

            messages.success(req, "Thanks for joining us! ")
            return redirect(homepage)
        else:
            messages.warning(req, "Invalid ")
            return redirect(signinpage)
    else:
        messages.warning(req, "Invalid ")
        return redirect(signinpage)


def signinpage(req):

    return  render(req,"signin.html")

def userlogout(req):
    del req.session['USERNAME']
    del req.session['PASSWORD1']
    messages.success(req,"Logged Out Successfully ")
    return redirect(signinpage)


def savebookslot(req):
    if req.method=="POST":
        a=req.POST.get('Bservices')
        b=req.POST.get('Bname')
        c=req.POST.get('Bnumber')
        d=req.POST.get('Bbread')
        e=req.POST.get('Bsex')
        f=req.POST.get('Bdate')
        g=req.POST.get('Btime')
        h=req.POST.get('Bmessage')
        i=req.POST.get('Bage')
        obj=BookslotDB(Bservices=a,Bname=b,Bnumber=c,Bbread=d,Bsex=e,Bdate=f,Btime=g,Bmessage=h,Bage=i)
        obj.save()
        messages.success(req,"Your Slot Booking has been successfully reserved!")
        return redirect(homepage)


def booking_pdf(request, booking_id):
    booking = get_object_or_404(BookslotDB, pk=booking_id)
    # Create a HttpResponse object with PDF mime type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking_id}.pdf"'

    # Create a canvas
    pdf = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = styles['Title']
    title_style.fontSize = 24  # Increase title font size

    # Body style
    body_style = styles['BodyText']
    body_style.fontSize = 12  # Increase body text font size

    # Title
    title = Paragraph("Booking Details", styles['Title'])
    content = []

    # Booking Information
    booking_info = [
        [" "],
        ["Service:", str(booking.Bservices)],
        ["Customer :", booking.Bname],
        ["Customer Mobile :", booking.Bnumber],
        ["Customer Bread :", booking.Bbread],
        ["Check-in Date:", str(booking.Bdate)],
        ["Check-in Time:", str(booking.Btime)],
        # Add more details as needed
    ]

    # Table Style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#77d8d8'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, '#77d8d8'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # Increase font size for all cells

    ])

    # Create Table
    booking_table = Table(booking_info)
    booking_table.setStyle(table_style)

    # Add elements to content
    content.append(title)
    content.append(booking_table)

    # Build PDF
    pdf.build(content)

    return response



def savecart(req):
    if req.method=="POST":
        a=req.POST.get('username')
        b=req.POST.get('productname')
        c=req.POST.get('quantity')
        d=req.POST.get('totalprice')
        e=req.POST.get('price')

        obj=CartDb(username=a,productname=b,quantity=c,totalprice=d,price=e)
        obj.save()
        messages.success(req, "Added to your shopping cart")
        return redirect(homepage)




def singleitem(req,Fid):
    data=FoodDB.objects.get(id=Fid)
    fd = FoodDB.objects.all()


    return render(req,"singleitem.html",{'data':data,'fd':fd})


def singlepageacc(req,Aid):
    cata=AccessoriesDB.objects.get(id=Aid)
    Acc=AccessoriesDB.objects.all()


    return render(req,"singlepageacc.html",{'cata':cata,'Acc':Acc})


def cartdetails(req):
    cart=CartDb.objects.filter(username=req.session['USERNAME'])
    shipping_charge = 0
    total_price = 0
    Total_amount = 0
    for i in cart:
        total_price = total_price + i.totalprice
        if total_price > 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        Total_amount = total_price + shipping_charge
    return render(req,"cart.html",{'cart':cart,'total_price':total_price,'shipping_charge':shipping_charge,'Total_amount':Total_amount})


def Deletecart(req, cartid):
    cart = CartDb.objects.filter(id=cartid)
    cart.delete()
    messages.error(req,"Item removed..!")
    return redirect(cartdetails)

def singlepet(req,Pid):
    bre = BreadDB.objects.all()
    pet=BreadDB.objects.get(id=Pid)

    return render(req,"singlepet.html",{'pet':pet,'bre':bre})

def checkoutpage(req):
    cata=CartDb.objects.all()
    cart=CartDb.objects.filter(username=req.session['USERNAME'])
    shipping_charge = 0
    total_price = 0
    Total_amount = 0
    for i in cart:
        total_price = total_price + i.totalprice
        if total_price > 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        Total_amount = total_price + shipping_charge
    return render(req,"checkout.html",{'cart':cart,'total_price':total_price,'shipping_charge':shipping_charge,'Total_amount':Total_amount,'cata':cata})


def saveorder(req):
    if req.method == "POST":
        a = req.POST.get('Name')
        b = req.POST.get('Email')
        c = req.POST.get('Place')
        d = req.POST.get('Address')
        e = req.POST.get('Mobile')
        f = req.POST.get('Message')
        g = req.POST.get('Price')
        h = req.POST.get('Productname')
        i = req.POST.get('Quantity')
        obj = OrderDb(Name=a, Email=b, Place=c, Address=d, Mobile=e, Message=f, Price=g,Productname=h,Quantity=i,)
        obj.save()
        return redirect(paymentpage)

def feedbacknotification(req):
    data=OrderDb.objects.all()
    order = OrderDb.objects.filter(Name=req.session['USERNAME'])
    cata=BookslotDB.objects.all()
    booking=BookslotDB.objects.filter(Bname=req.session['USERNAME'])




    return render(req,"feedbacknotification.html",{'order':order,'data':data,'cata':cata,'booking':booking})


def savefeedback(req):
    if req.method=="POST":
        a=req.POST.get('Fname')

        b=req.POST.get('Fphone')

        c=req.POST.get('Fmessage')
        obj=FeedbackDB(Fname=a,Fphone=b,Fmessage=c)
        obj.save()
        messages.success(req,"Thanks for your valuable feedback")
        return redirect(feedbacknotification)

def singleservice(req,Sid):
    Ser=Service1DB.objects.get(id=Sid)
    ser=Service1DB.objects.all()


    return render(req,"singleservice.html",{'Ser':Ser,'ser':ser})


def bookings(req,Bid):
    cart=CartDb.objects.filter(username=req.session['USERNAME'])
    Ser = Service1DB.objects.get(id=Bid)


    return render(req, "bookings.html",{'cart':cart,'Ser':Ser})









def paymentpage(req):
    #retrieve the checkoutdb object with the specified Id
    customer = OrderDb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    payy=customer.Price

    #convert the amount to paise(smallest currency unit)
    amount=int(payy*100)      #Assuming payment amount in rupees

    #convert amount to string for printing
    payy_str=str(amount)

   #printing each character of the payment amount
    for i in payy_str:
        print(i)

    if req.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_6KrFZyQoYiZXpF','Pxl1R9B4slDn1iy5HGXrOgmI'))
        payment= client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})

    return render(req,"payment.html",{'customer':customer,'payy_str':payy_str})


