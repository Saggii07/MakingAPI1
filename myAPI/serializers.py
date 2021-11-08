from django.contrib.auth import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import Advisor, Booking
from django.contrib.auth.models import User

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'advisor_name',
            'advisor_photo_url'
        )
        model= Advisor




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =(
            'username',
            'email'
            
        )

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50,min_length=6)
    password = serializers.CharField(max_length = 50,write_only=True)

    class Meta:
        model = User
        fields = ('id','username','email','password')

    def validate(self, attrs):
        username = attrs.get('username',None)
        email = attrs.get('email',None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exists')})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'user_id',
            'adviser_id',
            'booked_call_at'
        )
        model = Booking







        

# class GetadviserSerializer(serializers.ModelSerializer):
#         advisor_list=Advisor.objects.all()
#         class Meta:
#             model=Advisor
#             fields(
#                 'advisor_name',
#                 'advisor_photo_url'

#             )
        

    # def get(self,request):
    #     advisor1=Advisor.objects.all()
    #     serializer=AdvisorSerializer(advisor1,many=True)
    #     serializers.