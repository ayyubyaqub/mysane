import email
from rest_framework import serializers
from .helpers import send_otp_mobile  
from .models import *

class   UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model=User
        fields=['id','email','password','phone','first_name','last_name','gender','city','marital_status','dob']
        extra_kwargs = {'password': {'write_only': True},'id':{'read_only':True}}
    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], phone=validated_data['phone'],first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'],dob=validated_data['dob'])
        user.set_password(validated_data['password'])
        user.save()
        send_otp_mobile(user.phone,user)
        return user
    def update(self, instance, validated_data):
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.city=validated_data.get('city',instance.city)
        instance.marital_status=validated_data.get('marital_status',instance.marital_status)
        instance.dob=validated_data.get('dob',instance.dob)
        instance.save()
        return instance  


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
        instance.save()
        return instance    


class College_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model=College_detail
        fields=['id','user','college_name','degree','university','stream','From','to','grades','city']
        extra_kwargs = {'id':{'read_only':True}}
        

    def create(self, validated_data):
        obj=College_detail.objects.create(user=validated_data['user'], college_name=validated_data['college_name'],
        degree=validated_data['degree'], university=validated_data['university'], stream=validated_data['stream'], From=validated_data['From'],
         to=validated_data['to'], grades=validated_data['grades'],city=validated_data['city'])
    
        obj.save()
        return obj

    def update(self, instance, validated_data):
        instance.college_name=validated_data.get('college_name',instance.college_name)
        instance.degree=validated_data.get('degree',instance.degree)
        instance.university=validated_data.get('university',instance.university)
        instance.stream=validated_data.get('stream',instance.stream)
        instance.From=validated_data.get('From',instance.From)
        instance.to=validated_data.get('to',instance.to)
        instance.grades=validated_data.get('grades',instance.grades)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
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
        instance.save()
        return instance      


class ProfessionalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=professional_detail
        fields=['id','user','company_name','designation','From','to','location','work_responsibility']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        profe_detail=professional_detail.objects.create(user=validated_data['user'], company_name=validated_data['company_name'],designation=validated_data['designation'],From=validated_data['From'],to=validated_data['to'],location=validated_data['location'],work_responsibility=validated_data['work_responsibility'],)
        profe_detail.save()
        return profe_detail

    def update(self, instance, validated_data):
        instance.company_name=validated_data.get('company_name',instance.company_name)
        instance.designation=validated_data.get('designation',instance.designation)
        instance.From=validated_data.get('From',instance.From)
        instance.to=validated_data.get('to',instance.to)
        instance.location=validated_data.get('location',instance.location)
        instance.work_responsibility=validated_data.get('work_responsibility',instance.work_responsibility)
        instance.save()
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
        instance.save()
       
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
        instance.save()
       
        return instance  


class user_volunteershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_volunteership
        fields=['id','user','organisation_name','volunteer_title','volunteer_desc','volunteer_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        skill=user_volunteership.objects.create(user=validated_data['user'], volunteer_title=validated_data['volunteer_title'],volunteer_desc=validated_data['volunteer_desc'],volunteer_date=validated_data['volunteer_date'],organisation_name=validated_data['organisation_name'],)
        skill.save()
        return skill

    def update(self, instance, validated_data):
        instance.volunteer_title=validated_data.get('volunteer_title',instance.volunteer_title)
        instance.volunteer_desc=validated_data.get('volunteer_desc',instance.volunteer_desc)
        instance.volunteer_date=validated_data.get('volunteer_date',instance.volunteer_date)
        instance.organisation_name=validated_data.get('organisation_name',instance.organisation_name)
        instance.save()
       
        return instance 


class user_fellowshipshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_fellowship
        fields=['id','user','fellowship_title','organisation_name','fellowship_desc','fellowship_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        userfellowship=user_fellowship.objects.create(user=validated_data['user'], fellowship_title=validated_data['fellowship_title'],fellowship_desc=validated_data['fellowship_desc'],fellowship_date=validated_data['fellowship_date'],organisation_name=validated_data['organisation_name'],)
        userfellowship.save()
        return userfellowship

    def update(self, instance, validated_data):
        instance.fellowship_title=validated_data.get('fellowship_title',instance.fellowship_title)
        instance.fellowship_desc=validated_data.get('fellowship_desc',instance.fellowship_desc)
        instance.fellowship_date=validated_data.get('fellowship_date',instance.fellowship_date)
        instance.organisation_name=validated_data.get('organisation_name',instance.organisation_name)
        instance.save()
        return instance 


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_career
        fields=['id','user','title','company_name','location','date','description']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        usercareer=user_career.objects.create(user=validated_data['user'], title=validated_data['title'], company_name=validated_data['company_name'],location=validated_data['location'],date=validated_data['date'],description=validated_data['description'])
        usercareer.save()
        return usercareer

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.company_name=validated_data.get('company_name',instance.company_name)
        instance.location=validated_data.get('location',instance.location)
        instance.date=validated_data.get('date',instance.date)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance 


class user_socialmediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_social_media
        fields=['id','user','plateform','link']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        user_socialmedia=user_social_media.objects.create(user=validated_data['user'],plateform=validated_data['plateform'],link=validated_data['link'])
        user_socialmedia.save()
        return user_socialmedia

    def update(self, instance, validated_data):
        instance.plateform=validated_data.get('plateform',instance.plateform)
        instance.link=validated_data.get('link',instance.link)      
        instance.save()
        return instance 


class user_industrySerializer(serializers.ModelSerializer):
    class Meta:
        model=user_industry
        fields=['id','user','organisation_name','position','start_date','remark']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        obj=user_industry.objects.create(user=validated_data['user'],organisation_name=validated_data['organisation_name'],position=validated_data['position'],start_date=validated_data['start_date'],remark=validated_data['remark'])
        obj.save()
        return obj

    def update(self, instance, validated_data):
        instance.organisation_name=validated_data.get('organisation_name',instance.organisation_name)
        instance.position=validated_data.get('position',instance.position)      
        instance.start_date=validated_data.get('start_date',instance.start_date)           
        instance.remark=validated_data.get('remark',instance.remark)      
        instance.save()
        return instance 



class user_certificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_certification
        fields=['id','user','certification_name','certification_completion_id','certification_url','issue_date','expiry_date']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        obj=user_certification.objects.create(user=validated_data['user'],
        
        certification_name=validated_data['certification_name'],
        certification_completion_id=validated_data['certification_completion_id'],
        certification_url=validated_data['certification_url'],
        issue_date=validated_data['issue_date'],
        expiry_date=validated_data['expiry_date'],
       )
        obj.save()
        return obj        



class user_preference_Serializer(serializers.ModelSerializer):
    class Meta:
        model=user_preference
        fields=['id','user','prefered_job_type','prefered_job_location']
        extra_kwargs = {'id':{'read_only':True}}

    def create(self, validated_data):
        obj=user_preference.objects.create(user=validated_data['user'],prefered_job_type=validated_data['prefered_job_type'],   prefered_job_location=validated_data['prefered_job_location'],
       )
        obj.save()
        return obj        
