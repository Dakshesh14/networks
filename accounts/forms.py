from .models import UserModel
from django.contrib.auth.forms import UserCreationForm

class UserModelCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','phone','profile_pic']