import email
from rest_framework import serializers
from .helpers import send_otp_mobile  
from .models import *

class   UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password','phone','first_name','last_name','gender']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], phone=validated_data['phone'],first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'],)
        user.set_password(validated_data['password'])
        user.save()
        send_otp_mobile(user.phone,user)
        return user



class Education_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education_detail
        fields=['user','school_name','qualification','board','field','From','to','grades','city']
    def create(self, validated_data):
        education_detail=Education_detail.objects.create(user=validated_data['user'], school_name=validated_data['school_name'],
        qualification=validated_data['qualification'], board=validated_data['board'], field=validated_data['field'], From=validated_data['From'],
         to=validated_data['to'], grades=validated_data['grades'],city=validated_data['city'])
    
        education_detail.save()
        return education_detail



class SkillSerializer(serializers.ModelSerializer):
    pass
