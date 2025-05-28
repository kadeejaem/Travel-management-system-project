from django.db import models
from django.contrib.auth.models import User

# Vendor Model
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Package(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)  # vendor user
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False) 
    def __str__(self):
        return self.title

class Booking(models.Model):
    DESTINATIONS = [
        ('1', 'Dubai'),
        ('2', 'Maldives'),
        ('3', 'Bali'),
        ('3', 'India'),
        ('3', 'Australia'),
        ('3', 'Thailand'),
        

    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_time = models.DateTimeField()
    destination = models.CharField(max_length=1, choices=DESTINATIONS)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.get_destination_display()}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField(blank=True)
