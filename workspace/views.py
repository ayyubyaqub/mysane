from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from workspace.models import work_space
from workspace.serializers import work_spaceSerializer
# Create your views here.
class Work_space_view(APIView):
    def get(self,request,pk=None):
        if pk!=None:
            obj=work_space.objects.filter(id=pk).order_by('id')
            obj_data=work_spaceSerializer(obj,many=True)
            return JsonResponse({'status':200,'data':obj_data.data})
        obj=work_space.objects.all().order_by('id')
        obj_data=work_spaceSerializer(obj,many=True)
        return JsonResponse({'status':200,'data':obj_data.data})    

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

