

from django.contrib.auth.models import User

from django.shortcuts import render
from rest_framework import generics,serializers
from rest_framework.views import APIView
from .models import Advisor, Booking
from .serializers import AdvisorSerializer, RegistrationSerializer,BookingSerializer
from rest_framework.response import Response
from rest_framework import status
import uuid

# Create your views here.


# add Advisors
class ListAdvisor(generics.ListCreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer

class DetailAdvisor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


#user register api view with default registration and login with token
class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"Errors": serializers.get_error_detail}, status=status.HTTP_400_BAD_REQUEST)



#Get The Advisors List for
class AdviserList(APIView):

    def get(self,pk):
        user=User.objects.get(pk=pk)
        advisor = Advisor.objects.values('id','advisor_name','advisor_photo_url',)
        serializer= AdvisorSerializer(advisor,many=True)
        
        return Response(serializer.data,user.id)

# for Booking Adviser used model with fielsds user_id and and advisor id for booking (foreign key)
class BookedAdvisor(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookedAdvisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# For Booked Advisor list

class BookedAdvisorlist(generics.RetrieveUpdateDestroyAPIView):
    def get(self,pk):
        user=User.objects.get(pk=pk)
        booked_advisor_list = Booking.objects.all()
        serializer=BookingSerializer(booked_advisor_list,many=True)
        return Response(serializer.data,user.id)





