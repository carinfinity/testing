from django.contrib import admin
from myapp.models import newCar, upcomingCar, listingCar, usedCar, appointment, testemonial, NewsLetter, contactus
# Register your models here.


@admin.register(newCar)
class newCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'carname', 'cardesc', 'carprice', 'carrating', 'carlaunchdate', 'carmileage',
                    'carfueltype', 'carcc', 'carseatingcapacity', 'cartransmissiontype', 'carbodytype', 'carfrontbrake', 'carrearbrake', 'carfrontsuspension',
                    'carrearsuspension', 'carsteeringtype', 'carsteeringcolumn', 'carsteeringgeartype', 'carimagefront', 'carimageright',
                    'carimageleft', 'carimageback', 'carimagecolor1', 'carimagecolor2', 'carimagecolor3', 'date']


@admin.register(upcomingCar)
class upcomingCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'carname', 'cardesc', 'carprice', 'carrating', 'carlaunchdate', 'carmileage',
                    'carfueltype', 'carcc', 'carseatingcapacity', 'cartransmissiontype', 'carbodytype', 'carfrontbrake', 'carrearbrake', 'carfrontsuspension',
                    'carrearsuspension', 'carsteeringtype', 'carsteeringcolumn', 'carsteeringgeartype', 'carimagefront', 'carimageright',
                    'carimageleft', 'carimageback', 'carimagecolor1', 'carimagecolor2', 'carimagecolor3', 'date']


@admin.register(listingCar)
class listingCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'caruserfirstname', 'caruserlastname', 'caruseremail', 'carusermobile', 'caruseraddress', 'carname', 'carmodel',
                    'cardesc', 'carprice',
                    'carlaunchdate', 'carmileage',
                    'carfueltype', 'carcc', 'carseatingcapacity', 'cartransmissiontype', 'carbodytype', 'carimagefront', 'carimageright',
                    'carimageleft', 'carimageback', 'date']


@admin.register(usedCar)
class usedCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'carname', 'cardesc', 'carprice', 'carrating', 'carlaunchdate', 'carmileage',
                    'carfueltype', 'carcc', 'carseatingcapacity', 'cartransmissiontype', 'carbodytype', 'carfrontbrake', 'carrearbrake', 'carfrontsuspension',
                    'carrearsuspension', 'carsteeringtype', 'carsteeringcolumn', 'carsteeringgeartype', 'carimagefront', 'carimageright',
                    'carimageleft', 'carimageback', 'date']

@admin.register(appointment)
class appointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'caruserfirstname', 'caruserlastname', 'caruseremail', 'carusermobile', 'caruseraddress', 'carname', 'carmodel',
                    'carnumber',
                    'carlaunchdate', 'carimagefront', 'carimageright', 'carimageleft', 'carimageback', 'date', 'time']


@admin.register(testemonial)
class testemonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'useremail', 'usermobile', 'review', 'imagefront']


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(contactus)
class contactusAdmin(admin.ModelAdmin):
    list_display = ['id', 'usernames', 'useremails', 'usersubject', 'usermessage']