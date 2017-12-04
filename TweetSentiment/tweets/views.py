from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'tweets/index.html')

def home(request):
    context = {
        'test' : "happy thanksgiving my dudes",
        }
    return render(request,'tweets/home.html',context)