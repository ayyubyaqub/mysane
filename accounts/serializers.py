import email
from rest_framework import serializers
from .helpers import send_otp_mobile  
from .models import *

class   UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','phone','first_name','last_name','gender','dob']
        extra_kwargs = {'password': {'write_only': True},'id':{'read_only':True}}
    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], phone=validated_data['phone'],first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'],dob=validated_data['dob'])
        user.set_password(validated_data['password'])
        user.save()
        send_otp_mobile(user.phone,user)
        return user



class Education_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education_detail
        fields=['id','user','school_name','qualification','board','field','From','to','grades','city']
        extra_kwargs = {'id':{'read_only':True}}
        

    def create(self, validated_data):
        education_detail=Education_detail.objects.create(user=validated_data['user'], school_name=validated_data['school_name'],
        qualification=validated_data['qualification'], board=validated_data['board'], field=validated_data['field'], From=validated_data['From'],
         to=validated_data['to'], grades=validated_data['grades'],city=validated_data['city'])
    
        education_detail.save()
        return education_detail

    def update(self, instance, validated_data):
        instance.school_name=validated_data.get('school_name',instance.school_name)
        instance.qualification=validated_data.get('qualification',instance.qualification)
        instance.board=validated_data.get('board',instance.board)
        instance.field=validated_data.get('field',instance.field)
        instance.From=validated_data.get('From',instance.From)
        instance.to=validated_data.get('to',instance.to)
        instance.grades=validated_data.get('grades',instance.grades)
        instance.city=validated_data.get('city',instance.city)
        return instance    



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=['id','user','skill']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        skill=Skill.objects.create(user=validated_data['user'], skill=validated_data['skill'])
        skill.save()
        return skill

    def update(self, instance, validated_data):
        instance.skill=validated_data.get('skill',instance.skill)
        return instance      



class ProfessionalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=professional_detail
        fields=['id','user','company_name','designation','From','to','is_currently_working','location','work_responsibility']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        profe_detail=professional_detail.objects.create(user=validated_data['user'], company_name=validated_data['company_name'],designation=validated_data['designation'],From=validated_data['From'],to=validated_data['to'],is_currently_working=validated_data['is_currently_working'],location=validated_data['location'],work_responsibility=validated_data['work_responsibility'],)
        profe_detail.save()
        return profe_detail

    def update(self, instance, validated_data):
        instance.company_name=validated_data.get('company_name',instance.company_name)
        instance.designation=validated_data.get('designation',instance.designation)
        instance.From=validated_data.get('From',instance.From)
        instance.to=validated_data.get('to',instance.to)
        instance.is_currently_working=validated_data.get('is_currently_working',instance.is_currently_working)
        instance.location=validated_data.get('location',instance.location)
        instance.work_responsibility=validated_data.get('work_responsibility',instance.work_responsibility)
        return instance      


class User_projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_project
        fields=['id','user','project_title','project_desc','project_link']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        skill=user_project.objects.create(user=validated_data['user'], project_title=validated_data['project_title'],project_desc=validated_data['project_desc'],project_link=validated_data['project_link'],)
        skill.save()
        return skill

    def update(self, instance, validated_data):
        instance.project_title=validated_data.get('project_title',instance.project_title)
        instance.project_desc=validated_data.get('project_desc',instance.project_desc)
        instance.project_link=validated_data.get('project_link',instance.project_link)
       
        return instance  



class User_leadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_leadership
        fields=['id','user','leadership_title','leadership_desc','leadership_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        skill=user_leadership.objects.create(user=validated_data['user'], leadership_title=validated_data['leadership_title'],leadership_desc=validated_data['leadership_desc'],leadership_date=validated_data['leadership_date'],)
        skill.save()
        return skill

    def update(self, instance, validated_data):
        instance.project_title=validated_data.get('leadership_title',instance.leadership_title)
        instance.project_desc=validated_data.get('leadership_desc',instance.leadership_desc)
        instance.project_link=validated_data.get('leadership_date',instance.leadership_date)
       
        return instance  




class user_volunteershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_volunteership
        fields=['id','user','volunteer_title','volunteer_desc','volunteer_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        skill=user_volunteership.objects.create(user=validated_data['user'], volunteer_title=validated_data['volunteer_title'],volunteer_desc=validated_data['volunteer_desc'],volunteer_date=validated_data['volunteer_date'],)
        skill.save()
        return skill

    def update(self, instance, validated_data):
        instance.volunteer_title=validated_data.get('volunteer_title',instance.volunteer_title)
        instance.volunteer_desc=validated_data.get('volunteer_desc',instance.volunteer_desc)
        instance.volunteer_date=validated_data.get('volunteer_date',instance.volunteer_date)
       
        return instance 


class user_fellowshipshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_fellowship
        fields=['id','user','fellowship_title','fellowship_desc','fellowship_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        userfellowship=user_fellowship.objects.create(user=validated_data['user'], fellowship_title=validated_data['fellowship_title'],fellowship_desc=validated_data['fellowship_desc'],fellowship_date=validated_data['fellowship_date'],)
        userfellowship.save()
        return userfellowship

    def update(self, instance, validated_data):
        instance.fellowship_title=validated_data.get('fellowship_title',instance.fellowship_title)
        instance.fellowship_desc=validated_data.get('fellowship_desc',instance.fellowship_desc)
        instance.fellowship_date=validated_data.get('fellowship_date',instance.fellowship_date)
        return instance 


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_career
        fields=['id','user','title','emp_type','company_name','location','start_date','end_date','description']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        usercareer=user_career.objects.create(user=validated_data['user'], emp_type=validated_data['emp_type'],company_name=validated_data['company_name'],location=validated_data['location'],start_date=validated_data['start_date'],end_date=validated_data['end_date'],description=validated_data['description'])
        usercareer.save()
        return usercareer

    def update(self, instance, validated_data):
        instance.emp_type=validated_data.get('emp_type',instance.emp_type)
        instance.company_name=validated_data.get('company_name',instance.company_name)
        instance.location=validated_data.get('location',instance.location)
        instance.is_currently_working=validated_data.get('is_currently_working',instance.is_currently_working)
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.end_date=validated_data.get('end_date',instance.end_date)
        instance.description=validated_data.get('description',instance.description)
        return instance 


