from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self,email,username,password,**extra_fileds):
        """
        Create and save a user with the given username,email,and password
        """
        if not email:
            raise ValueError('The given email must be set')
        email=self.normalize_email(email)
        username=self.normalize_username(username)
        user=self.model(email=email,username=username,**extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,username='',password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,username,password,**extra_fields)

    def create_superuser(self,email,username='',password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self._create_user(email,username,password,**extra_fields)
    

class User(AbstractUser):
    # 로그인은 email로 하는걸로 한다. 
    # unique 메일 중복 체크
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)

    username=models.CharField(max_length=30)

    USERNAME_FIELD='email'
    # 필수로 받고 싶은 필드를 넣기 원래 소스 코드엔 email 필드가 들어가지만, 우리는 로그인을 이메일로 하니깐...
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return "<%d %d>" % (self.pk,self.email)