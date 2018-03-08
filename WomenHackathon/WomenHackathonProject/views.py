import sys
from django.shortcuts import render
sys.setrecursionlimit(1500)

def index(request):
    return render(request,'WomenHackathonProject/index.html',context = None)

def user_login(request):
    return render(request,'WomenHackathonProject/index.html',context = None)

def user_registration(request):
    return render(request,'WomenHackathonProject/index.html',context = None)