from ast import Pass
from requests import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework.views import APIView 
from django.http import JsonResponse
from .helpers import *
from django.contrib.auth import login #authenticate
from rest_framework import status
from django.db.models import Q
from rest_framework import viewsets

def authenticate(username=None, password=None,):
    try:
        user = User.objects.get(
            (Q(email=username) | Q(phone=username)))
        print(user,18)    
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
        else:
            return None


class  RegisterView(APIView):
    def post(self,request):
        print('i am here 30')
        print(request.data)
        try:
            serializer=UserSerializer(data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                    }
                )
            print('OK')
            serializer.save()
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'an email and otp send on your email and number'
                     }
                )
        except Exception as e :
            print(32)
            print(e)    
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )

class LoginView(APIView):
    def get(self , request):
        if request.user.is_authenticated:
            userserializer=UserSerializer(request.user)
            print(userserializer.data['id'],12)
            return JsonResponse({'status':True,'user_data':userserializer.data})
        return JsonResponse({'status':False})

    def post(self, request, format=None):
        data = request.data
        print(data)
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        print(user,16)
        if user is not None:
            if user.is_active:
                login(request, user)
                userserializer=UserSerializer(user)
                print(userserializer.data)

                return JsonResponse({'status':True,'user_data':userserializer.data})
            else:
                return JsonResponse({
                    'status':False,
                    'msg':'Invalid crediential'
                })    

        else:
            return JsonResponse({
                    'status':False,
                    'error':'something went wrong ayyub'
                })  
    
class VerifyOtp(APIView):
    def post(self, request):
        try:
            data=request.data
            print(data)
            user_obj=User.objects.get(phone=data.get('phone'))
            otp=data.get('otp')
            if user_obj.otp == otp:
                user_obj.is_phone_varified=True
                user_obj.save()
                userserializer=UserSerializer(user_obj)
                return JsonResponse({'status':True,'user_data':userserializer.data})
            return JsonResponse({
                    'status':403,
                    'msg':'your otp is wrong'
                })    

        except Exception as e:
            print(e)  
        return  JsonResponse({
                    'status':404,
                    'error':'something went wrong'
                })          

    def patch(self, request):
        try :
            data=request.data
            user_obj=User.objects.filter(phone=data.get('phone'))
            if not user_obj.exists():
                return JsonResponse({
                    'status':404,
                    'error':'something went wrong'
                })

            status,time=  send_otp_mobile(data.get('phone'),user_obj[0])  
            if status:
                return JsonResponse({
                    'status':200,
                    'msg':'new otp sent'
                })
            return JsonResponse({
                    'status':404,
                    'error':f'try after {time} seconds'
                })    
        except Exception as e:
            print(e)


class educationdetail(APIView):
    def get(self,request):
        educationdetaildata=Education_detail.objects.all()
        educationdetaildata=Education_detailSerializer(educationdetaildata,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':educationdetaildata.data
                        
                    }
                )

    def post(self,request):
        print(request.user)
        data=request.data
        print(data)
    
        try:
            serializer=Education_detailSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            print('OK')
            resp=serializer.save()
           
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Education detail is saved'
                     }
                )
        except Exception as e :
            print(178)
            print(e,179)    
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request):
        print('i')
        data=request.data
        print(data)
        id=int(data['id'])   
        edu_detail=Education_detail.objects.get(id=id)
        print(edu_detail)
        edu_detail.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':'congratulations you are in delete'
                        
                    }
                )

    def put(self, request, pk, format=None):
        print('hi i am in 212')
        print(pk,213)
        educationdetail = Education_detail.objects.get(id=pk)
        print(educationdetail)
        print(request.data)
        data={'school_name':'abcd'}
        try:
            serializer = Education_detailSerializer(educationdetail, data=data)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'user_data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class skill(APIView):
    pass 