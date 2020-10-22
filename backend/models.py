from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.models import UserModel

class Post(models.Model):
    user = models.ForeignKey(UserModel,related_name='user',on_delete=models.CASCADE)
    content = models.TextField(max_length=1080,null=False)
    photo = models.ImageField(upload_to='images/posts',blank=True,null=True)
    photo_thumbnail = ImageSpecField(source='photo',processors=[ResizeToFill(100, 50)],format='JPEG',options={'quality': 60})
    data_uploaded = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} posted {self.content}"


class Following(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='currentUser')
    following = models.ManyToManyField(UserModel,related_name='following')
    followers = models.ManyToManyField(UserModel,related_name='follower')

    def __str__(self):
        return self.user