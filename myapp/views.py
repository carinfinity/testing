from django.shortcuts import HttpResponseRedirect, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignUpForm, ListingForm, AppointmentForm
from .models import newCar, upcomingCar, listingCar, usedCar, appointment, testemonial, UserOTP, NewsLetter, contactus
from .models import appointment as user_appointments
from django.conf import settings
from django.core.mail import send_mail
import random
import joblib



# Create your views here.


def index(request):
    products = newCar.objects.all()
    uproducts = upcomingCar.objects.all()
    listing = listingCar.objects.all()
    usedcar = usedCar.objects.all()
    review = testemonial.objects.all()[:3]
    return render(request, 'myapp/index.html', {'review': review, 'product': products, 'product1': uproducts, 'product2': listing, 'product3': usedcar})


def base(request):
    return render(request, 'myapp/base.html')


def user_login(request):
    if request.method == "POST":
        fg = LoginForm(request=request, data=request.POST)
        if fg.is_valid():
            username = fg.cleaned_data['username']
            password = fg.cleaned_data['password']
            print(username)
            print(password)
            User = authenticate(username=username, password=password)
            print(User)
            if User is not None:
                login(request, User)
                messages.success(request, 'loged in successfully')
                return HttpResponseRedirect('/')
                print(User)
    else:
        fg = LoginForm()

    return render(request, 'myapp/login.html', {'form': fg})


def user_signup(request):
    print(request.method)
    if request.method == "POST":
        get_otp = request.POST.get('otp')
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'myapp/signup.html', {'otp': True, 'usr': usr})
        
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            username = fm.cleaned_data.get('email')
            usr = User.objects.get(email=username)
            usr.username = username
            usr.is_active = False
            usr.save()
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            subject = 'welcome to Car Infinity - Verify Your Email'
            message = f'Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['hrishikesh.kini.35@gmail.com', ]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'myapp/signup.html', {'otp': True, 'usr': usr})

    else:
        fm = SignUpForm

    return render(request, 'myapp/signup.html', {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def listing(request):
    print(request.method)
    if request.method == 'POST':
        caruserfirstname = request.user.first_name
        caruserlastname = request.user.last_name
        caruseremail = request.user.email
        carusermobile = request.POST['carusermobile']
        caruseraddress = request.POST['caruseraddress']
        carname = request.POST['carname']
        carmodel = request.POST['carmodel']
        cardesc = request.POST['cardesc']
        carprice = request.POST['carprice']
        carlaunchdate = request.POST['carlaunchdate']
        carmileage = request.POST['carmileage']
        carfueltype = request.POST['carfueltype']
        carcc = request.POST['carcc']
        carseatingcapacity = request.POST['carseatingcapacity']
        cartransmissiontype = request.POST['cartransmissiontype']
        carbodytype = request.POST['carbodytype']
        carimagefront = request.FILES['carimagefront']
        carimageright = request.FILES['carimageright']
        carimageleft = request.FILES['carimageleft']
        carimageback = request.FILES['carimageback']
        reg = listingCar(caruserfirstname=caruserfirstname, caruserlastname=caruserlastname, caruseremail=caruseremail,
                         carusermobile=carusermobile, caruseraddress=caruseraddress, carname=carname, carmodel=carmodel, cardesc=cardesc,
                         carprice=carprice, carlaunchdate=carlaunchdate, carmileage=carmileage, carfueltype=carfueltype, carcc=carcc,
                         carseatingcapacity=carseatingcapacity, cartransmissiontype=cartransmissiontype, carbodytype=carbodytype,
                         carimagefront=carimagefront, carimageright=carimageright, carimageleft=carimageleft, carimageback=carimageback)
        reg.save()
    else:
        print("form invalid")
    fg = listingCar.objects.filter(
        caruseremail__exact=request.user.email)
    print(fg)
    return render(request, 'myapp/listing.html', {'listing': fg})


def deletelisting(request, id):
    if request.method == 'POST':
        pi = listingCar.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/listing/')


def myapp():
    y = 0


@login_required(login_url='/login/')
def appointment(request):
    dates = ''
    if request.method == 'POST':
        if 'check' in request.POST:
            dates = request.POST['datess']
            myapp.y = dates
            print(myapp.y)
            print(dates)

        if 'submit' in request.POST:
            caruserfirstname = request.user.first_name
            caruserlastname = request.user.last_name
            caruseremail = request.user.email
            carusermobile = request.POST['carusermobile']
            caruseraddress = request.POST['caruseraddress']
            carname1 = request.POST['carname1']
            carmodel = request.POST['carmodel']
            carnumber = request.POST['carnumber']
            carlaunchdate = request.POST['carlaunchdate']
            carimagefront = request.FILES['carimagefront']
            carimageright = request.FILES['carimageright']
            carimageleft = request.FILES['carimageleft']
            carimageback = request.FILES['carimageback']
            date1 = myapp.y
            time = request.POST['owner']
            print(time)

            print(carimageback)
            reg1 = user_appointments(caruserfirstname=caruserfirstname, caruserlastname=caruserlastname, caruseremail=caruseremail,
                                     carusermobile=carusermobile, caruseraddress=caruseraddress, carname=carname1, carmodel=carmodel,
                                     carnumber=carnumber, carlaunchdate=carlaunchdate,
                                     carimagefront=carimagefront, carimageright=carimageright, carimageleft=carimageleft, carimageback=carimageback,
                                     date=date1, time=time)
            reg1.save()
            subject = 'welcome to Car Infinity - Appointments'
            message = f'Hi {request.user.first_name},Your appointment has been booked successfully.\n Car : {carname1} {carmodel} \n Date: {date1} \n Time : {time} \n Please Keep the Below code as an identity \n 123890'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['hrishikesh.kini.35@gmail.com', ]
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponseRedirect('/addappointment/')

    usershow = user_appointments.objects.filter(date=dates)
    print(usershow)
    if dates == '':
        j = 0
    else:
        j = 1
    leng = len(usershow)
    return render(request, 'myapp/appointment.html', {'date': usershow, 'len': leng, 'j': j, 'dates': dates})

def addappointment(request):
    newobj = newCar.objects.all()
    return render(request, 'myapp/bookappointment.html', {'obj': newobj})

# this car showing pages


def newcarpage(request):
    newobj = newCar.objects.all()
    return render(request, 'myapp/newcar.html', {'obj': newobj})


def upcomingcarpage(request):
    newobj = upcomingCar.objects.all()
    return render(request, 'myapp/upcoming.html', {'obj': newobj})


def listingcarpage(request):
    newobj = listingCar.objects.all()
    return render(request, 'myapp/listingcar.html', {'obj': newobj})


def usedcarpage(request):
    newobj = usedCar.objects.all()
    return render(request, 'myapp/usedcar.html', {'obj': newobj})

# this is car detai;s pages


def newcardetailpage(request, id):
    newobj = newCar.objects.filter(id=id)
    return render(request, 'myapp/cardetail.html', {'obj': newobj})


def upcomingcardetailpage(request, id):
    newobj = upcomingCar.objects.filter(id=id)
    return render(request, 'myapp/upcomingcardetail.html', {'obj': newobj})


def usedcardetailpage(request, id):
    newobj = usedCar.objects.filter(id=id)
    return render(request, 'myapp/usedcardetail.html', {'obj': newobj})


def listingcardetailpage(request, id):
    newobj = listingCar.objects.filter(id=id)
    return render(request, 'myapp/listingdetail.html', {'obj': newobj})


def aboutus(request):
    return render(request, 'myapp/aboutus.html')


def ourteam(request):
    return render(request, 'myapp/team.html')


def testing(request):
    if request.method == 'POST':
        present=request.POST['present_price']
        km=request.POST['kms_driven']
        owner = request.POST['owner']
        year = request.POST['year']
        fuel = request.POST['fuel']
        seller = request.POST['seller']
        transmission = request.POST['transmission']
        print(present,km,owner,year,fuel,seller,transmission)
    return render(request, 'myapp/test.html')


def searchfunc(request):
    query = request.GET['query']
    products = newCar.objects.filter(carname__icontains=query)
    uproducts = upcomingCar.objects.filter(carname__icontains=query)
    listing = listingCar.objects.filter(carname__icontains=query)
    usedcar = usedCar.objects.filter(carname__icontains=query)

    return render(request, 'myapp/search.html', {'product': products, 'product1': uproducts, 'product2': listing, 'product3': usedcar})


def contactuss(request):
    if request.method == 'POST':
        names=request.POST['username']
        emails=request.POST['useremail']
        subjects = request.POST['usersubject']
        messages = request.POST['usermessage']
        print(names, emails, subjects, messages)
        reg = contactus(usernames=names, useremails=emails, usersubject=subjects,
                         usermessage=messages)
        reg.save()
    return render(request, 'myapp/contact.html')

def testimonial(request):
    review = testemonial.objects.all()
    return render(request, 'myapp/testimonials.html', {'review':review})

def sellcar(request):
    return render(request, 'myapp/sellcar.html')

def buycar(request):
    return render(request, 'myapp/buycar.html')


#machine learming model
def predictprice(request):
    regressor = joblib.load('mlmodel.sav')
    lis = []
    ans =""
    if request.method == 'POST':
        lis.append(request.POST['present_price'])
        lis.append(request.POST['kms_driven'])
        lis.append(request.POST['owner'])
        lis.append(request.POST['year'])
        lis.append(request.POST['fuel'])
        lis.append(request.POST['seller'])
        lis.append(request.POST['transmission'])
        print(lis)
        ans = regressor.predict([lis])
        print(ans)
    return render(request,'myapp/predict.html', {'ans':ans})

    #newsletter
def newsletter(request):
    if request.method == 'POST':
        emails = request.POST['email']
        reg = NewsLetter(email = emails)
        reg.save()
        print(emails)
    return HttpResponseRedirect('/')

def addtestemonial(request):
    if request.method == 'POST':
        userfirstname = request.user.first_name
        userlastname = request.user.last_name
        useremail = request.user.email
        usermobile = request.POST['carusermobile']
        review = request.POST['reviewa']
        imagefront = request.FILES['carimageback']
        reg = testemonial(userfirstname = userfirstname, userlastname = userlastname, useremail = useremail,
        usermobile = usermobile, review = review, imagefront = imagefront)
        reg.save()
        print(usermobile, review)
        
    return render(request,'myapp/addtesti.html')