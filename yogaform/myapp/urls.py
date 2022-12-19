from django.urls import path
from myapp import views

urlpatterns=[
    path('https://web-production-7af1.up.railway.app/', views.yogaform,name='yogaform'), 
    path('https://web-production-7af1.up.railway.app/update', views.updateform,name='updateform'), 
    path('completePayment',views.completePayment,name='completepayment')
]