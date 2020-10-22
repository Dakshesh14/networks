from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponseRedirect,reverse
from django.http import JsonResponse


from .forms import UserModelCreationForm
from .models import UserModel

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('backend:index'))

        return render(request,'accounts/login.html',{
            'message':'Invalid Credentails'
        })

    else:
        print(request.user)
        return render(request,'accounts/login.html',{
            'message':''
        })

def register_view(request):
    if request.method == 'POST':
        form = UserModelCreationForm(request.POST,request.FILES or None)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request,'accounts/register.html',{
                "message":"Passwords didn't match"
            })

        if UserModel.objects.filter(email=email).exists():
            return render(request,'accounts/register.html',{
                'message':'Email already in use'
            })

        if UserModel.objects.filter(phone=phone).exists():
            return render(request,'accounts/register.html',{
                'message':'Phone already in use'
            })      

        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.email = email
                obj.save()
                user = authenticate(request,email=email,password=password1)
                login(request,user)

            except:
                return render(request,'accounts/register.html',{
                    'message':'Some unknown error occurred.'
                })  


            return HttpResponseRedirect(reverse('backend:index'))
        
        else:
            return render(request,'accounts/register.html',{
                'message':'Password is too short.'
            })  

    else:
        return render(request,'accounts/register.html',{
            'message':'',
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))