from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from workspace.models import work_space,project,Task
from workspace.serializers import work_spaceSerializer,projectSerializer,taskSerializer
# Create your views here.
class Work_space_view(APIView):
    def get(self,request,pk=None):
        if pk!=None:
            obj=work_space.objects.filter(user__id=pk).order_by('id')
            obj_data=work_spaceSerializer(obj,many=True)
            return JsonResponse({'status':200,'data':obj_data.data})
        
        return JsonResponse({'status':404,'error':'Not Found'})    

    def post(self,request):
        data=request.data
        print(data)
        serializer=work_spaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'workspace created' })
        print(serializer.errors)    
        return  JsonResponse({'status':500,'msg':'something went wrong'})   

    def put(self,request,pk):
        obj=work_space.objects.get(id=pk)
        serializer=work_spaceSerializer(obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return ({'status':200,'msg':'workspace updated'})
        return JsonResponse({'status':500,'msg':'something went wrong'})    

    def delete(self,request,pk):
        obj=work_space.objects.get(id=pk)
        obj.delete()
        return JsonResponse({'status':200,'msg':'deleted'})


class project_view(APIView):
    def get(self,request,pk=None):
        if pk!=None:
            obj=project.objects.filter(user__id=pk).order_by('id')
            obj_data=projectSerializer(obj,many=True)
            return JsonResponse({'status':200,'data':obj_data.data})
        
        return JsonResponse({'status':404,'error':'Not Found'})    

    def post(self,request):
        data=request.data
        print(data)
        serializer=projectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'project created' })
        print(serializer.errors)    
        return  JsonResponse({'status':500,'msg':serializer.errors})   

    def put(self,request,pk):
        obj=project.objects.get(id=pk)
        serializer=projectSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'project updated'})
        return JsonResponse({'status':500,'msg':'something went wrong'})    

    def delete(self,request,pk):
        obj=project.objects.get(id=pk)
        obj.delete()
        return JsonResponse({'status':200,'msg':'deleted'})



class task_view(APIView):   
    def get(self,request,pk=None):
        if pk!=None:
            obj=Task.objects.filter(user__id=pk).order_by('id')
            obj_data=taskSerializer(obj,many=True)
            return JsonResponse({'status':200,'data':obj_data.data})
        
        return JsonResponse({'status':404,'error':'Not Found'})    

    def post(self,request):
        data=request.data
        print(data)
        serializer=taskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'task created' })
        print(serializer.errors)    
        return  JsonResponse({'status':500,'msg':serializer.errors})   

    def put(self,request,pk):
        obj=Task.objects.get(id=pk)
        serializer=taskSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'msg':'task updated'})
        return JsonResponse({'status':500,'msg':'something went wrong'})    

    def delete(self,request,pk):
        obj=Task.objects.get(id=pk)
        obj.delete()
        return JsonResponse({'status':200,'msg':'deleted'}) 




