from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class newCar(models.Model):
    carname = models.CharField(max_length=255)
    cardesc = models.TextField(max_length=500)
    carprice = models.CharField(max_length=255)
    carrating = models.CharField(max_length=255)
    carlaunchdate = models.CharField(max_length=255)
    carmileage = models.CharField(max_length=255)
    carfueltype = models.CharField(max_length=255)
    carcc = models.CharField(max_length=255)
    carseatingcapacity = models.CharField(max_length=255)
    cartransmissiontype = models.CharField(max_length=255)
    carbodytype = models.CharField(max_length=255)
    carfrontbrake = models.CharField(max_length=255)
    carrearbrake = models.CharField(max_length=255)
    carfrontsuspension = models.CharField(max_length=255)
    carrearsuspension = models.CharField(max_length=255)
    carsteeringtype = models.CharField(max_length=255)
    carsteeringcolumn = models.CharField(max_length=255)
    carsteeringgeartype = models.CharField(max_length=255)
    carimagefront = models.ImageField(upload_to="myappnewcar")
    carimageright = models.ImageField(upload_to="myappnewcar")
    carimageleft = models.ImageField(upload_to="myappnewcar")
    carimageback = models.ImageField(upload_to="myappnewcar")
    carimagecolor1 = models.ImageField(upload_to="myappnewcar")
    carimagecolor2 = models.ImageField(upload_to="myappnewcar")
    carimagecolor3 = models.ImageField(upload_to="myappnewcar")
    date = models.DateTimeField(auto_now_add=True)


class upcomingCar(models.Model):
    carname = models.CharField(max_length=255)
    cardesc = models.TextField(max_length=500)
    carprice = models.CharField(max_length=255)
    carrating = models.CharField(max_length=255)
    carlaunchdate = models.CharField(max_length=255)
    carmileage = models.CharField(max_length=255)
    carfueltype = models.CharField(max_length=255)
    carcc = models.CharField(max_length=255)
    carseatingcapacity = models.CharField(max_length=255)
    cartransmissiontype = models.CharField(max_length=255)
    carbodytype = models.CharField(max_length=255)
    carfrontbrake = models.CharField(max_length=255)
    carrearbrake = models.CharField(max_length=255)
    carfrontsuspension = models.CharField(max_length=255)
    carrearsuspension = models.CharField(max_length=255)
    carsteeringtype = models.CharField(max_length=255)
    carsteeringcolumn = models.CharField(max_length=255)
    carsteeringgeartype = models.CharField(max_length=255)
    carimagefront = models.ImageField(upload_to="myappupcomingcar")
    carimageright = models.ImageField(upload_to="myappupcomingcar")
    carimageleft = models.ImageField(upload_to="myappupcomingcar")
    carimageback = models.ImageField(upload_to="myappupcomingcar")
    carimagecolor1 = models.ImageField(upload_to="myappupcomingcar")
    carimagecolor2 = models.ImageField(upload_to="myappupcomingcar")
    carimagecolor3 = models.ImageField(upload_to="myappupcomingcar")
    date = models.DateTimeField(auto_now_add=True)


class listingCar(models.Model):
    caruserfirstname = models.CharField(max_length=255)
    caruserlastname = models.CharField(max_length=255)
    caruseremail = models.CharField(max_length=255)
    carusermobile = models.CharField(max_length=255)
    caruseraddress = models.TextField(max_length=500)
    carname = models.CharField(max_length=255)
    carmodel = models.CharField(max_length=255)
    cardesc = models.TextField(max_length=500)
    carprice = models.CharField(max_length=255)
    carlaunchdate = models.CharField(max_length=255)
    carmileage = models.CharField(max_length=255)
    carfueltype = models.CharField(max_length=255)
    carcc = models.CharField(max_length=255)
    carseatingcapacity = models.CharField(max_length=255)
    cartransmissiontype = models.CharField(max_length=255)
    carbodytype = models.CharField(max_length=255)
    carimagefront = models.ImageField(upload_to="mylistingcar")
    carimageright = models.ImageField(upload_to="mylistingcar")
    carimageleft = models.ImageField(upload_to="mylistingcar")
    carimageback = models.ImageField(upload_to="mylistingcar")
    date = models.DateTimeField(auto_now_add=True)


class usedCar(models.Model):
    carname = models.CharField(max_length=255)
    cardesc = models.TextField(max_length=500)
    carprice = models.CharField(max_length=255)
    carrating = models.CharField(max_length=255)
    carlaunchdate = models.CharField(max_length=255)
    carmileage = models.CharField(max_length=255)
    carfueltype = models.CharField(max_length=255)
    carcc = models.CharField(max_length=255)
    carseatingcapacity = models.CharField(max_length=255)
    cartransmissiontype = models.CharField(max_length=255)
    carbodytype = models.CharField(max_length=255)
    carfrontbrake = models.CharField(max_length=255)
    carrearbrake = models.CharField(max_length=255)
    carfrontsuspension = models.CharField(max_length=255)
    carrearsuspension = models.CharField(max_length=255)
    carsteeringtype = models.CharField(max_length=255)
    carsteeringcolumn = models.CharField(max_length=255)
    carsteeringgeartype = models.CharField(max_length=255)
    carimagefront = models.ImageField(upload_to="myusedcar")
    carimageright = models.ImageField(upload_to="myusedcar")
    carimageleft = models.ImageField(upload_to="myusedcar")
    carimageback = models.ImageField(upload_to="myusedcar")
    date = models.DateTimeField(auto_now_add=True)



class appointment(models.Model):
    caruserfirstname = models.CharField(max_length=255)
    caruserlastname = models.CharField(max_length=255)
    caruseremail = models.CharField(max_length=255)
    carusermobile = models.CharField(max_length=255)
    caruseraddress = models.TextField(max_length=500)
    carname = models.CharField(max_length=255)
    carmodel = models.CharField(max_length=255)
    carnumber = models.CharField(max_length=255)
    carlaunchdate = models.CharField(max_length=255)
    carimagefront = models.ImageField(upload_to="myappointment")
    carimageright = models.ImageField(upload_to="myappointment")
    carimageleft = models.ImageField(upload_to="myappointment")
    carimageback = models.ImageField(upload_to="myappointment")
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)


class testemonial(models.Model):
    userfirstname = models.CharField(max_length=255)
    userlastname = models.CharField(max_length=255)
    useremail = models.CharField(max_length=255)
    usermobile = models.CharField(max_length=255)
    review = models.TextField(max_length=500)
    imagefront = models.ImageField(upload_to="testemonial")

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()


class NewsLetter(models.Model):
	email = models.CharField(max_length=255)

class contactus(models.Model):
    usernames = models.CharField(max_length=255)
    useremails = models.CharField(max_length=255)
    usersubject = models.CharField(max_length=255)
    usermessage = models.TextField(max_length=500)
    