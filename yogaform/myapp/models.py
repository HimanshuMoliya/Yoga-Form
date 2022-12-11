from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField(max_length=254)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    batch=models.ForeignKey('Batch',on_delete=models.CASCADE,null=False)

class Batch(models.Model):
    batch_id=models.AutoField(primary_key=True)
    SESSION_CHOICES = (
        ('M1', '6-7 AM'),
        ('M2', '7-8 AM'),
        ('M3', '8-9 AM'),
        ('E', '5-6 PM')
    )
    time=models.CharField(max_length=20, choices=SESSION_CHOICES, null=False)

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(null=False)
    date=models.DateTimeField(null=False)
    payment_successful=models.BooleanField()

class Admission(models.Model):
    admission_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    payment_id=models.ForeignKey('Payment',on_delete=models.CASCADE)
    batch_id=models.ForeignKey('Batch',on_delete=models.CASCADE)

