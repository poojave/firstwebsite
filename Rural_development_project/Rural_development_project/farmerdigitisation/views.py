import sys
from django.shortcuts import render
sys.setrecursionlimit(1500)

def index(request):
    return render(request,'Farmerdigitisation/index.html',context = None)

def farmer_login(request):
    return render(request,'Farmerdigitisation/index.html',context = None)

def farmer_registration(request):
    return render(request,'Farmerdigitisation/index.html',context = None)