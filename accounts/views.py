from ast import Pass
from functools import partial
from http.client import HTTPResponse
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

from rest_framework import filters
from rest_framework import viewsets
def authenticate(username=None, password=None,):
    try:
        user = User.objects.get(
            (Q(email=username) | Q(phone=username)))
        print(user,18)    
    except User.DoesNotExist:
        return 404
    else:
        if user.check_password(password):
            return user
        else:
            return 401


class  RegisterView(APIView):
    def post(self,request):
        print('i am here 30')
        print(request.data) 
        try:
            serializer=UserSerializer(data=request.data)
            if not serializer.is_valid():
                print(serializer.errors,34)
                return JsonResponse(
                    {
                        'status':403,
                        'error':str(serializer.errors)
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
        password = data.get('login_password', None)
        user = authenticate(username=username, password=password)
        if user==404:
            return JsonResponse({
                    'status':404,
                    'msg':'User DoesNot Exist'
                    })  
        elif(user==401):
            return JsonResponse({
                    'status':401,
                    'msg':'Wrong Password'
                    })

        elif user is not None:
            if user.is_active:
                if user.is_phone_varified:
                    login(request, user)
                    userserializer=UserSerializer(user)
                    return JsonResponse({'status':True,'user_data':userserializer.data})
                else:
                    return JsonResponse({
                    'status':405,
                    'msg':'Please verify your phone number'
                    })    

            else:
                return JsonResponse({
                    'status':403,
                    'msg':'You are blocked by admin'
                })    

        else:
            return JsonResponse({
                    'status':500,
                    'msg':'something went wrong'
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
                    'error':'mobile does not exist'
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
    def get(self,request,pk=None):
        print(pk)
        if pk != None:
            print(pk,306)
            obj=Education_detail.objects.filter(user__id=pk).order_by('id')
            obj_data=Education_detailSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        return JsonResponse(
                    {
                        'status':404,
                        'data':'Not Found'
                        
                    }
                )

    def post(self,request):
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
    

    def delete(self, request,pk):
   
        edu_detail=Education_detail.objects.get(id=pk)
        edu_detail.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':'congratulations you are in delete'
                        
                    }
                )

    def put(self, request, pk, format=None):
        educationdetail = Education_detail.objects.get(id=pk)
    
        try:
            serializer = Education_detailSerializer(educationdetail, data=request.data,partial=True)
        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'user_data':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})  


class college_detail_view(APIView):
    def get(self,request,pk=None):
        print(pk)
        if pk != None:
            print(pk,306)
            obj=College_detail.objects.filter(user__id=pk).order_by('id')
            print(obj,236)
            objdata=College_detailSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':objdata.data
                        
                    }
                )
  
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )

    def post(self,request):
        data=request.data
        try:
            serializer=College_detailSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
          
            resp=serializer.save()
            print(resp)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Education detail is saved'
                     }
                )
        except Exception as e :
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
   
        object=College_detail.objects.get(id=pk)
        object.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':'congratulations you are in delete'
                        
                    }
                )

    def put(self, request, pk, format=None):
        object = College_detail.objects.get(id=pk)
    
        try: 
            serializer = College_detailSerializer(object, data=request.data,partial=True)
        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'user_data':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})  


class skill(APIView):
    def get(self,request,pk=None):
        print(304)
        if pk != None:
            print(pk,306)
            skills=Skill.objects.filter(user__id=pk).order_by('id')
            skillsdata=SkillSerializer(skills,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':skillsdata.data
                        
                    }
                )

        skills=Skill.objects.all()
        skillsdata=SkillSerializer(skills,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':skillsdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data 
        print(data)   
        try:
            serializer=SkillSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
           
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your skill detail is saved'
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
    

    def delete(self, request,pk):
        print(pk)   
        skill=Skill.objects.get(id=pk)
        skill.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your project detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        skilldetail = Skill.objects.get(id=pk)
        try:
            serializer = SkillSerializer(skilldetail, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_skill':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})    


class professional_Detail(APIView):
    def get(self,request,pk=None):
        print(319)
        if pk != None:
            print(pk,321)
            obj=professional_detail.objects.filter(user__id=pk).order_by('id')
            objdata=ProfessionalDetailSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':objdata.data
                        
                    }
                )
        
        prof_detail=professional_detail.objects.all()
        skillsdata=ProfessionalDetailSerializer(prof_detail,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':skillsdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data)
    
        try:
            serializer=ProfessionalDetailSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
           
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your professional detail is saved'
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
    

    def delete(self, request,pk):
        print(pk)   
        prof_detail=professional_detail.objects.get(id=pk)
        prof_detail.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your professional detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        prof_detail = professional_detail.objects.get(id=pk)
        try:
            serializer = ProfessionalDetailSerializer(prof_detail, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_skill':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})     



class user_project_view(APIView):
    def get(self,request,pk=None):
        print(406)
        if pk != None:
            print(pk,408)
            userproject=user_project.objects.filter(user__id=pk).order_by('id')
            userprojectdata=User_projectSerializer(userproject,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':userprojectdata.data
                        
                    }
                )
        
        userproject=user_project.objects.all()
        userprojectdata=User_projectSerializer(userproject,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':userprojectdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data
    
        try:
            serializer=User_projectSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your project detail is saved'
                     }
                )
        except Exception as e : 
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        userproject=user_project.objects.get(id=pk)
        userproject.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your project detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        prof_detail = user_project.objects.get(id=pk)
        try:
            serializer = User_projectSerializer(prof_detail, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_skill':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})               



class user_leadership_view(APIView):
    def get(self,request,pk=None):
        print(406)
        if pk != None:
            print(pk,408)
            userleadership=user_leadership.objects.filter(user__id=pk).order_by('id')
            userleadershipdata=User_leadershipSerializer(userleadership,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':userleadershipdata.data
                        
                    }
                )
        
        userleadership=user_leadership.objects.all()
        userleadershipdata=User_leadershipSerializer(userleadership,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':userleadershipdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data)
        try:
            serializer=User_leadershipSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your leadership detail is saved'
                     }
                )
        except Exception as e : 
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        userleadership=user_leadership.objects.get(id=pk)
        userleadership.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your leadership detail is deleted'
                        
                    }
                )
                

    def put(self, request, pk, format=None):
        userleadership = user_leadership.objects.get(id=pk)
        print(request.data,pk)
        try:
            serializer = User_leadershipSerializer(userleadership, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_leadership':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})             


class user_volunteership_view(APIView):
    def get(self,request,pk=None):
        print(406)
        if pk != None:
            print(pk,408)
            uservolunteership=user_volunteership.objects.filter(user__id=pk).order_by('id')
            uservolunteershipdata=user_volunteershipSerializer(uservolunteership,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':uservolunteershipdata.data
                        
                    }
                )
        
        uservolunteership=user_volunteership.objects.all()
        uservolunteershipdata=user_volunteershipSerializer(uservolunteership,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':uservolunteershipdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data)
        try:
            serializer=user_volunteershipSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your volunteership detail is saved'
                     }
                )
        except Exception as e : 
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        uservolunteership=user_volunteership.objects.get(id=pk)
        uservolunteership.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your volunteership detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        uservolunteership = user_volunteership.objects.get(id=pk)
        try:
            serializer = user_volunteershipSerializer(uservolunteership, data=request.data ,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_leadership':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})                 


class user_fellowship_view(APIView):
    def get(self,request,pk=None):
        print(406)
        if pk != None:
            print(pk,408)
            userfellowship=user_fellowship.objects.filter(user__id=pk).order_by('id')
            userfellowshipdata=user_fellowshipshipSerializer(userfellowship,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':userfellowshipdata.data
                        
                    }
                )
        
        userfellowship=user_fellowship.objects.all()
        userfellowshipdata=user_fellowshipshipSerializer(userfellowship,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':userfellowshipdata.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data)
        try:
            serializer=user_fellowshipshipSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your volunteership detail is saved'
                     }
                )
        except Exception as e : 
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_fellowship.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your volunteership detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_fellowship.objects.get(id=pk)
        try:
            serializer = user_fellowshipshipSerializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_fellowship':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})            


class user_career_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            print(pk,737)
            obj=user_career.objects.filter(user__id=pk).order_by('id')
            obj_data=CareerSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        
        obj=user_career.objects.all()
        obj_data=CareerSerializer(obj,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data,761)
        try:
            serializer=CareerSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors,766)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            print(resp,774)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Career detail is saved'
                     }
                )
        except Exception as e : 
            print(e,783)
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_career.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your career detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_career.objects.get(id=pk)
        try:
            serializer = CareerSerializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_career':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})                

    
class ChangePassword(APIView):
     def post(self, request):
        try:
            data=request.data
            user_obj=User.objects.get(phone=data.get('phone'))
            password1=data.get('password1')
            password12=data.get('password2')
            if password1 == password12:
                user_obj.set_password(password1)
                user_obj.save()
                userserializer=UserSerializer(user_obj)
                return JsonResponse({'status':True,'user_data':userserializer.data})
            return JsonResponse({
                    'status':403,
                    'msg':'Please Enter Same Password'
                })    

        except Exception as e:
            print(e)  
        return  JsonResponse({
                    'status':404,
                    'error':'something went wrong'+str(e)
                })          


class user_social_media_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            print(pk,737)
            obj=user_social_media.objects.filter(user__id=pk).order_by('id')
            obj_data=user_socialmediaSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        
        obj=user_social_media.objects.all()
        obj_data=user_socialmediaSerializer(obj,many=True)
        return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data,874)
        try:
            serializer=user_socialmediaSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors,766)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            print(resp,774)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Social Media detail is saved'
                     }
                )
        except Exception as e : 
            print(e,783)
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_social_media.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your social media detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_social_media.objects.get(id=pk)
        try:
            serializer = user_socialmediaSerializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_socialmedia':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})                 


class user_industry_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            print(pk,935)
            obj=user_industry.objects.filter(user__id=pk).order_by('id')
            obj_data=user_industrySerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data,874)
        try:
            serializer=user_industrySerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors,766)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            print(resp,774)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Social Media detail is saved'
                     }
                )
        except Exception as e : 
            print(e,783)
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_industry.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your social media detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_industry.objects.get(id=pk)
        print(request.data)
        try:
            serializer = user_industrySerializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e)
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_industry':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})     


class update_profile_view(APIView):
    def patch(self, request, pk, format=None):
        print(pk)
        try:
            user = User.objects.get(id=pk)
            print(request.data)
            print(request.method)
            serializer = UserSerializer(user, data=request.data,partial=True)
            print(serializer)
            if serializer.is_valid():
                print(1025)
                serializer.save()
                return JsonResponse({'status':True,'user_data':serializer.data})
            print(serializer.errors)    
        except Exception as e:  
            print(e)
            return Response({'status':False,'error':str(e)})
        
        return JsonResponse({'error':serializer.errors, 'status':False})


class user_certification_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            obj=user_certification.objects.filter(user__id=pk).order_by('id')
            print(obj)
            obj_data=user_certificationSerializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data,874)
        try:
            serializer=user_certificationSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors,766)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            print(resp,774)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Social Media detail is saved'
                     }
                )
        except Exception as e : 
            print(e,783)
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_certification.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your social media detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_certification.objects.get(id=pk)
        try:
            serializer = user_certificationSerializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e) 
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_certification':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})                


class user_preference_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            obj=user_preference.objects.filter(user__id=pk).order_by('id')
            print(obj)
            obj_data=user_preference_Serializer(obj,many=True)
            return JsonResponse(
                    {
                        'status':200,
                        'data':obj_data.data
                        
                    }
                )
        
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )

    def post(self,request):
        data=request.data
        print(data,874)
        try:
            serializer=user_preference_Serializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors,766)
                return JsonResponse(
                    {
                        'status':403,
                        'errors':serializer.errors
                        
                    }
                )
            resp=serializer.save()
            print(resp,774)
            return JsonResponse(
                    {
                        'status':200, 
                        'msg':'Your Social Media detail is saved'
                     }
                )
        except Exception as e : 
            print(e,783)
            return JsonResponse(
                {
                    'status':404,
                    'error':'something went wrong'
                }
            )
    

    def delete(self, request,pk):
        print(pk)   
        obj=user_preference.objects.get(id=pk)
        obj.delete()
        return JsonResponse(
                    {
                        'status':200,
                        'data':' your social media detail is deleted'
                        
                    }
                )

    def put(self, request, pk, format=None):
        obj = user_preference.objects.get(id=pk)
        try:
            serializer = user_preference_Serializer(obj, data=request.data,partial=True)

        except Exception as e:  
            print(e) 
            pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':True,'updated_industry':serializer.data})
        return JsonResponse({'status':False,'msg':serializer.errors})                


class professional_summery_view(APIView):
    def get(self,request,pk=None):
        if pk != None:
            obj=Skill.objects.filter(user__id=pk).order_by('id')
            obj_data=SkillSerializer(obj,many=True)
            list1=[{'Skill':obj_data.data}]
            
            obj=professional_detail.objects.filter(user__id=pk).order_by('id')
            obj_data=ProfessionalDetailSerializer(obj,many=True)
            list1.append({'professional_detail':obj_data.data})


            obj=user_project.objects.filter(user__id=pk).order_by('id')
            obj_data=User_projectSerializer(obj,many=True)
            list1.append({'user_project':obj_data.data})


            obj=user_leadership.objects.filter(user__id=pk).order_by('id')
            obj_data=User_leadershipSerializer(obj,many=True)
            list1.append({'user_leadership':obj_data.data})
            
            obj=user_volunteership.objects.filter(user__id=pk).order_by('id')
            obj_data=user_volunteershipSerializer(obj,many=True)
            list1.append({'user_volunteership':obj_data.data})


            obj=user_fellowship.objects.filter(user__id=pk).order_by('id')
            obj_data=user_fellowshipshipSerializer(obj,many=True)
            list1.append({'user_fellowship':obj_data.data})


            obj=user_career.objects.filter(user__id=pk).order_by('id')
            obj_data=CareerSerializer(obj,many=True)
            list1.append({'user_career':obj_data.data})
            
            obj=user_social_media.objects.filter(user__id=pk).order_by('id')
            obj_data=user_socialmediaSerializer(obj,many=True)
            list1.append({'user_social_media':obj_data.data})


            obj=user_industry.objects.filter(user__id=pk).order_by('id')
            obj_data=user_industrySerializer(obj,many=True)
            list1.append({'user_industry':obj_data.data})


            obj=user_certification.objects.filter(user__id=pk).order_by('id')
            obj_data=user_certificationSerializer(obj,many=True)
            list1.append({'user_certification':obj_data.data})


            obj=user_preference.objects.filter(user__id=pk).order_by('id')
            obj_data=user_preference_Serializer(obj,many=True)
            list1.append({'user_preference':obj_data.data})

            return JsonResponse(
                    {
                        'status':200,
                        'data':list1
                        
                    }
                )
        
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )


class educational_summery_view(APIView):

    def get(self,request,pk=None):
        if pk != None:
            obj=Education_detail.objects.filter(user__id=pk).order_by('id')
            obj_data=Education_detailSerializer(obj,many=True)
            list1=[{'School_detail':obj_data.data}]


            obj=College_detail.objects.filter(user__id=pk).order_by('id')
            obj_data=College_detailSerializer(obj,many=True)
            list1.append({'College_detail':obj_data.data})
            return JsonResponse(
                        {
                            'status':200,
                            'data':list1
                            
                        }
                    )
        
        return JsonResponse(
                    {
                        'status':404,
                        'data':'User Not Exist'
                        
                    }
                )



class PurchaseList(APIView):
    
    def get(self,request,pk):
        print(pk)

        userlist=User.objects.filter( Q(first_name__icontains=pk)|Q(last_name__icontains=pk)
        |Q(education_details__school_name__icontains=pk)
        |Q(education_details__qualification__icontains=pk)
        |Q(education_details__board__icontains=pk)
        |Q(education_details__field__icontains=pk)
        |Q(education_details__city__icontains=pk)
        |Q(college_details__college_name__icontains=pk)
        |Q(college_details__degree__icontains=pk)
        |Q(college_details__university__icontains=pk)
        |Q(college_details__stream__icontains=pk)
        |Q(college_details__city__icontains=pk)
        |Q(skill__skill__icontains=pk)
        |Q(professionaldetail__company_name__icontains=pk)
        |Q(professionaldetail__designation__icontains=pk)
        |Q(professionaldetail__location__icontains=pk)
        |Q(career__title__icontains=pk)
        |Q(career__company_name__icontains=pk)
        |Q(career__location__icontains=pk)
       
        ).distinct()
        print(userlist)
        userjson=UserSerializer(userlist,many=True)
        return JsonResponse({'status':200,'search_result':userjson.data})


# from rest_framework import generics
# class ProductList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer    
#     filter_backends = [filters.SearchFilter]
#     filterset_fields = ['first_name', 'last_name']


class resume_view(APIView):
    def get(self,request,pk):
        obj=resume.objects.filter(user=pk)
        serializer=resumeSerializer(obj)
        return JsonResponse({'status':200,'data':serializer.data })

    def post(self,request,pk):
        request.data['user']=pk
        serializer=resumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'resume uploaded' })
        print(serializer.errors)    
        return  JsonResponse({'status':500,'msg':serializer.errors})   





        