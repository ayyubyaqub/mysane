from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from accounts.manager import UserManager
from .manager import UserManager
from django.dispatch import receiver
from django.core.mail import send_mail
import uuid
from django.conf import settings


class User(AbstractUser):
    username=None
    first_name=models.CharField(max_length=50, null=True,blank=True)
    last_name=models.CharField(max_length=50, null  =True,blank=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=14,unique=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    marital_status=models.CharField(max_length=50,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    is_email_varified=models.BooleanField(default=False)
    is_phone_varified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,null=True,blank=True)
    email_varification_token=models.CharField(max_length=200,null=True,blank=True)
    forget_password_token=models.CharField(max_length=100,null=True,blank=True)
    last_login=models.DateTimeField(null=True,blank=True)

    objects=UserManager()

    USERNAME_FIELD= 'email'

    REQUIRED_FIELDS=[]
    def __str__(self):
        return str(self.phone)+' '+str(self.email)

@receiver(post_save,sender=User)
def send_email_token(sender ,instance , created ,**kwargs):
    if created:
        try:
            subject="Your email needs to be verified"
            message=f'hi click on the link to verify email http://localhost:8000/verify/{uuid.uuid4()}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[instance.email]
            send_mail(subject ,message ,email_from , recipient_list)

        except Exception as e:
            print(e)


class Education_detail(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='education_details',null=True,blank=True)
    school_name=models.CharField(max_length=100,null=True,blank=True)
    qualification=models.CharField(max_length=100,null=True,blank=True)
    board=models.CharField(max_length=100,null=True,blank=True)
    field=models.CharField(max_length=100,null=True,blank=True)
    From=models.DateField(null=True, blank=True)
    to=models.DateField(null=True, blank=True)
    grades=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):        
        return str(self.user)+' '+str(self.qualification)

  

class College_detail(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='college_details',null=True,blank=True)
    college_name=models.CharField(max_length=100,null=True,blank=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    university=models.CharField(max_length=100,null=True,blank=True)
    stream=models.CharField(max_length=100,null=True,blank=True)
    From=models.DateField(null=True, blank=True)
    to=models.DateField(null=True, blank=True)
    grades=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):        
        return str(self.user)+' '+str(self.degree)
  

class Skill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='skill')
    skill=models.CharField(max_length=255,null=True,blank=True)


class professional_detail(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='professionaldetail',null=True,blank=True)
    company_name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    From=models.DateField(null=True, blank=True)
    to=models.DateField(null=True, blank=True)
    location=models.TextField(null=True,blank=True)
    work_responsibility=models.TextField(null=True,blank=True)


class user_project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    project_title=models.CharField(max_length=255,null=True,blank=True)
    project_desc=models.TextField()
    project_link=models.TextField()


class user_leadership(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='leadership')
    leadership_title=models.CharField(max_length=255,null=True,blank=True)
    leadership_desc=models.TextField()
    leadership_date=models.DateField()


class user_volunteership(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='volunteership')
    volunteer_title=models.CharField(max_length=255,null=True,blank=True)
    organisation_name=models.CharField(max_length=255,null=True,blank=True)
    volunteer_desc=models.TextField()
    volunteer_date=models.DateField()


class user_fellowship(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='fellowship')
    fellowship_title=models.CharField(max_length=255,null=True,blank=True)
    organisation_name=models.CharField(max_length=255,null=True,blank=True)
    fellowship_desc=models.TextField()
    fellowship_date=models.DateField()


class user_career(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='career')
    title=models.CharField(max_length=255,null=True,blank=True)    
    company_name=models.CharField(max_length=255,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)


class user_social_media(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='socialmedia')
    plateform=models.CharField(max_length=255)
    link=models.TextField()


class user_industry(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='industry')
    organisation_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    start_date=models.DateField(null=True,blank=True)
    remark=models.TextField()


class user_certification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='certification')
    certification_name=models.CharField(max_length=255,null=True,blank=True)
    certification_completion_id=models.CharField(max_length=255,null=True,blank=True)
    certification_url=models.TextField(null=True, blank=True)
    issue_date=models.CharField(max_length=255,null=True,blank=True)
    expiry_date=models.CharField(max_length=255,null=True,blank=True)


class user_preference(models.Model):  
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='preference')
    prefered_job_type=models.CharField(max_length=255,null=True,blank=True)
    prefered_job_location=models.CharField(max_length=255,null=True,blank=True)
