from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime

# create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def service(request):
    return render(request, "service.html")
def contact(request):
    if request.method == 'POST':
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        return render(request, "home.html")
    else:
        form = ContactForm()
    return render(request,"contact.html", {'form':form})

   
def destination(request):
    return render(request, "destination.html")

def testimonials(request):
    return render(request, "testimonial.html")
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            usrnm = form.cleaned_data.get('username')
            pswrd = form.cleaned_data.get('password')
            user = authenticate(username=usrnm, password=pswrd)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {usrnm}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = SigninForm()
    return render(request, 'login.html', {'form': form})

def tlogout(request):
    logout(request)
    return redirect('home')




def package_list(request):
    packages = Package.objects.all().order_by('-created_at') 
    return render(request, 'packages_list.html', {'packages': packages})
                  
def book_tour(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date_time = parse_datetime(request.POST.get('date_time'))
        destination = request.POST.get('destination')
        message = request.POST.get('message')

        Booking.objects.create(
            name=name,
            email=email,
            date_time=date_time,
            destination=destination,
            message=message
        )
        return redirect('booking_success')

    return render(request, 'booking.html')    

def booking_success(request):
    return render(request, 'booking_success.html')    


def contact(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = ContactForm()
    
        return render(request,"contact.html",{'form':form})
    

def vendor_dashboard(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.vendor = request.user 
            package.save()
            return redirect('vendor_dashboard')  
    else:
        form = PackageForm()
    
  
    packages = request.user.package_set.all()

    return render(request, 'vendor_dashboard.html', {
        'form': form,
        'packages': packages,
    })

def v_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = RegisterForm()
    return render(request, 'vendor_signup.html', {'form': form})

def v_signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            usernm = form.cleaned_data.get('username')
            paswrd = form.cleaned_data.get('password')
            user = authenticate(username=usernm, password=paswrd)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {usernm}!")
                return redirect('vendor_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = SigninForm()
    return render(request, 'vendor_login.html', {'form': form})
