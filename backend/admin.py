from django.contrib import admin

from accounts.models import UserModel
from backend.models import Post, Following

admin.site.register(UserModel)
admin.site.register(Post)