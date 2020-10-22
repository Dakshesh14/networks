from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse

def index(request):
    return render(request, 'backend/index.html',{

    })