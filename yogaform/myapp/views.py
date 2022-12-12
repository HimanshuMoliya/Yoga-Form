from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import FormSerializer, UserSerializer

@api_view(['GET','POST'])
def form(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=FormSerializer(data=request.data)
        if serializer.is_valid():
           FormSerializer.save(request.data)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   