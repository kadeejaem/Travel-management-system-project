from django.contrib.auth.views import LogoutView
from django.urls import path
from .import views as v


urlpatterns = [
    path('base/',v.base,name='base'),
    path('',v.home,name='home'),
    path('about/',v.about,name='about'),
    path('service/',v.service,name='service'),
    path('contact/',v.contact,name='contact'),
    path('destination/',v.destination,name='destination'),  
    path('testimonial/',v.testimonials,name='testimonial'),    
    path('register/',v.register,name='register'),
    path('login/', v.signin, name='login'),
    path('logout/', v.logout, name='logout'),
    path('vendor_dashboard/', v.vendor_dashboard, name='vendor_dashboard'),
    path('booking/', v.book_tour, name='book_tour'),
    path('packages_list/',v.package_list,name='packages_list'),
    path('contact/',v.contact,name='contact'),
    path('booking-success/', v.booking_success, name='booking_success'),
    path('v_signup/', v.v_register, name='v_signup'),
    path('v_signin/', v.v_signin, name='v_signin'),
    path('logout/',v.tlogout, name='logout'),
]
    
    



    



