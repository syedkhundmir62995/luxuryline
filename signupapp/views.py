from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    return render(request,'signupapp/signup.html')