from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from myapp.views import newcarpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'myapp_index'),
    path('base/', views.base, name = 'myapp_base'),
    path('login/', views.user_login, name = 'myapp_user_login'),
    path('signup/', views.user_signup, name = 'myapp_user_signup'),
    path('logout/', views.user_logout, name = 'myapp_user_logout'),
    path('listing/', views.listing, name = 'myapp_listing'),
    path('delete/<int:id>/', views.deletelisting, name = 'deletelist'),
    path('appointment/', views.appointment, name = 'myapp_appointment'),
    path('addappointment/', views.addappointment, name = 'myapp_addappointment'),
    #this is car products urls
    path('newcarpage/', views.newcarpage, name = 'myapp_newcarpage'),
    path('upcomingcar/', views.upcomingcarpage, name = 'myapp_upcomingcarpage'),
    path('listingcarpage/', views.listingcarpage, name = 'myapp_listingcarpage'),
    path('usedcarpage/', views.usedcarpage, name = 'myapp_usedcarpage'),
    #this is car detail urls
    path('newcardetail/<int:id>', views.newcardetailpage, name = 'myapp_newcardetailpage'),
    path('upcomingcardetail/<int:id>', views.upcomingcardetailpage, name = 'myapp_newcardetailpage'),
    path('usedcardetail/<int:id>', views.usedcardetailpage, name = 'myapp_newcardetailpage'),
    path('listingcardetail/<int:id>', views.listingcardetailpage, name = 'myapp_newcardetailpage'),
    #additional pages
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('team/', views.ourteam, name = 'team'),
    path('test/', views.testing, name = 'testing'),
    path('search/', views.searchfunc, name = 'searchfunc'),
    path('contactus/', views.contactuss, name = 'contactus'),
    path('testimonials/', views.testimonial, name = 'testimonial'),
    path('sellcar/', views.sellcar, name = 'sellcar'),
    path('buycar/', views.buycar, name = 'buycar'),
    path('predict/', views.predictprice, name = 'predictprice'),
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('addtestemonial/', views.addtestemonial, name = 'addtestemonial'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)