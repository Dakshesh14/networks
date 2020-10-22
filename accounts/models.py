from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserModelManager(BaseUserManager):

    def create_user(self,email,username,profile_pic,phone,password=None):
        if not email:
            raise ValueError("Email can't be empty!")

        if not username:
            raise ValueError("Username can't be empty!")

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            phone=phone,
            profile_pic=profile_pic,
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,email,username,password):
        if not email:
            raise ValueError("Email can't be empty!")

        if not username:
            raise ValueError("Username can't be empty!")

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class UserModel(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=225,unique=True)
    username = models.CharField(max_length=225,unique=False)
    phone = models.CharField(max_length=10)
    profile_pic = ProcessedImageField(upload_to='images/userProfilePics',processors=[ResizeToFill(200, 200)],format='JPEG',options={'quality': 60})

    is_staff = models.BooleanField(default=False)

    objects = UserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.username
