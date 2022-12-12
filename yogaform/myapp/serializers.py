from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['user_id','first_name','last_name','age','email','contact_number','gender','batch']

class FormSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    contact_number = serializers.CharField() 
    gender=serializers.CharField()
    batch_id=serializers.IntegerField()
    amount=serializers.IntegerField()
    payment_successful=serializers.BooleanField()

    def save(self):
        f_name=self.get('first_name')
        l_name=self.get('last_name')
        a=self.get('age')
        e=self.get('email')
        cn=self.get('contact_number')
        g=self.get('gender')
        b=self.get('batch_id')
        amt=self.get('amount')
        p=self.get('payment_successful')
        User.objects.create(first_name=f_name,last_name=l_name,age=a,email=e,contact_number=cn,gender=g, batch_id=b)
        u_id=User.objects.order_by('-user_id')[0]
        Payment.objects.create(user_id=u_id,amount=amt,payment_successful=p)

        if(p=='True'):
            p_id=Payment.objects.order_by('-payment_id')[0]
            Admission.objects.create(payment_id=p_id,user_id=u_id,batch_id=b)
        

