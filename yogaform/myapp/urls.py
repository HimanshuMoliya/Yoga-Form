from django.urls import include, path
from myapp import views

urlpatterns=[
    path('', views.form), 
]