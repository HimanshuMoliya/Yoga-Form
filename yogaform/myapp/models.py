from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validate_age(value):
    if value < 18 or value > 65:
        raise ValidationError(
            ('Age must be between 18 and 65'),
            params={'value': value},
        )

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.PositiveIntegerField(validators=[validate_age])
    email=models.EmailField(max_length=25,unique='True')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid contact number")
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,unique='True') 

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    batch=models.ForeignKey('Batch',on_delete=models.CASCADE,null=False)

class Batch(models.Model):
    batch_id=models.IntegerField(primary_key=True)
    SESSION_CHOICES = (
        ('M1', '6-7 AM'),
        ('M2', '7-8 AM'),
        ('M3', '8-9 AM'),
        ('E', '5-6 PM')
    )
    time=models.CharField(max_length=20, choices=SESSION_CHOICES)

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(null=False)
    date=models.DateTimeField(auto_now_add=True)
    payment_successful=models.BooleanField()

class Admission(models.Model):
    admission_id=models.AutoField(primary_key=True)
    payment_id=models.ForeignKey('Payment',on_delete=models.CASCADE,null=False)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE,null=False)
    batch=models.ForeignKey('Batch',on_delete=models.CASCADE,null=False)

